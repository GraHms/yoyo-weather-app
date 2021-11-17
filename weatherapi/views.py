from django.http import JsonResponse

# Create your views here.
from weatherapi.schemas import WeatherRequestParams


def weather_view(request, city):
    request_params: WeatherRequestParams = WeatherRequestParams(city=city,
                                                                **request.GET.dict())

    return JsonResponse({"greetings": request_params.dict()})
