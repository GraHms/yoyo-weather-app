from django.http import  JsonResponse


# Create your views here.
def weather_view(request, city):
    days = int(request.GET.get('days', 1))
    return JsonResponse({"greetings":city})
