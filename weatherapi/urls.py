from django.urls import path
from . import views


urlpatterns = [
    path('locations/<str:city>/', views.weather_view),

]
