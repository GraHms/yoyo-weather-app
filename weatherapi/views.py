# This file includes the weather business logic and view serialization

import logging
import requests
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework.response import Response

from weatherapi.schemas import WeatherRequestParams
from weatherapi.serializers import WeatherSerializer

from yoyoweatherapp.settings import WEATHER_API_KEY


def compute_temperatures(weatherlist):

    # we take the first maximum as result
    max_temp = weatherlist[0]['day']["maxtemp_c"]
    # we take the first days avg temperature as defaull
    min_temp = weatherlist[0]['day']["mintemp_c"]
    all_avg_temp = []
    for res in weatherlist:
        _max_temp = res['day']["maxtemp_c"]
        _min_temp = res['day']["mintemp_c"]

        all_avg_temp.append(res['day']['avgtemp_c'])

        # we compare all other days with the first to find the maximum
        if _max_temp > max_temp:
            # replace if finds a new maximum
            max_temp = _max_temp
        # we compare all other days with the first to find the minimum
        if _min_temp < min_temp:
            # replace if finds a new minimum
            min_temp = _min_temp
        return max_temp, min_temp, all_avg_temp


def get_weather(input_values: WeatherRequestParams):
    weatherapi_basepath = "http://api.weatherapi.com/v1/forecast.json"

    try:
        params = {"key": WEATHER_API_KEY,
                  "q": input_values.city,
                  "days": input_values.days}

        result = requests.get(weatherapi_basepath, params=params)
        if result.status_code == 200:
            weatherlist = result.json().get('forecast')['forecastday']
            max_temp, min_temp, all_avg_temp = compute_temperatures(weatherlist)
            days = len(weatherlist)
            median_temp = (max_temp + min_temp) / 2
            # Average temperature = Sum of temperatures of all the days / *no. of days
            avg_temp = sum(all_avg_temp) / days
            data = {"minimum": min_temp, "maximum": max_temp, "average": round(avg_temp, 2),
                    "median": round(median_temp, 2)}
            return data, result.status_code
        else:
            # dynamically maps error messages and status code from weatherapi
            logging.exception(result)
            return {"message": result.json().get('error')['message']}, result.status_code

    except Exception as err:
        # in case of a network exception or something out of our api control
        logging.exception(err)
        Response({"message": err}, status=500)


@api_view(['GET'])
@renderer_classes([JSONRenderer, StaticHTMLRenderer])
def weather_view(request, city):
    # request values
    input_values: WeatherRequestParams = WeatherRequestParams(city=city,
                                                              **request.GET.dict())
    # api results
    result, status_code = get_weather(input_values=input_values)

    if status_code == 200:
        result: WeatherSerializer = WeatherSerializer(data=result)
        result.is_valid(raise_exception=True)
        result = result.data

    return Response(result, status=status_code)
