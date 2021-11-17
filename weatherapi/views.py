import logging

import requests
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, StaticHTMLRenderer
from rest_framework.response import Response

from weatherapi.schemas import WeatherRequestParams
from weatherapi.serializers import WeatherSerializer

# The method that fe
from yoyoweatherapp.settings import WEATHER_API_KEY


def get_weather(input_values: WeatherRequestParams):
    weatherapi_basepath = "http://api.weatherapi.com/v1/forecast.json"

    try:
        params = {"key": WEATHER_API_KEY,
                  "q": input_values.city,
                  "days": input_values.days}
        result = requests.get(weatherapi_basepath, params=params)
        if result.status_code == 200:
            weatherlist = result.json().get('forecast')['forecastday']
            max_temp = 0
            all_avg_temp = []
            min_temp = None
            days = len(weatherlist)
            for res in weatherlist:
                _max_temp = res['day']["maxtemp_c"]
                _min_temp = res['day']["mintemp_c"]

                all_avg_temp.append(res['day']['avgtemp_c'])

                if _max_temp > max_temp:
                    max_temp = _max_temp
                if min_temp is None:
                    min_temp = _min_temp
                else:
                    if _min_temp < min_temp:
                        min_temp = _min_temp

            median_temp = (max_temp + min_temp) / 2
            # Average temperature = Sum of temperatures of all the days / *no. of days
            avg_temp = sum(all_avg_temp) / days
            data = {"minimum": min_temp, "maximum": max_temp, "average": round(avg_temp, 2),
                    "median": round(median_temp, 2)}
            return data
    except Exception as err:
        logging.ERROR(err)


@api_view(['GET'])
@renderer_classes([JSONRenderer, StaticHTMLRenderer])
def weather_view(request, city):
    input_values: WeatherRequestParams = WeatherRequestParams(city=city,
                                                              **request.GET.dict())

    weather_data = get_weather(input_values=input_values)
    result: WeatherSerializer = WeatherSerializer(data=weather_data)
    result.is_valid()

    return Response(result.data)
