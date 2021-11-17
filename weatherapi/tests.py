from rest_framework import status
from rest_framework.test import APITestCase

from weatherapi.schemas import WeatherRequestParams
from weatherapi.views import get_weather


class WeatherTests(APITestCase):
    def test_method_not_allowed(self):
        response = self.client.post('/api/locations/maputo')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_resource_not_found(self):
        response = self.client.post('/api/locations/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_city(self):
        response = self.client.get('/api/locations/ggggdgdgd')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get("message"), "No matching location found.")

    def test_get_weather_api(self):
        input_values: WeatherRequestParams = WeatherRequestParams(city='maputo',
                                                                  days=2)

        result, status_code = get_weather(input_values=input_values)
        response = self.client.get('/api/locations/maputo?days=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, status_code)



