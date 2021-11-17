from django.urls import path
from . import views


urlpatterns = [
    path('locations/<city>', views.weather_view),

]
