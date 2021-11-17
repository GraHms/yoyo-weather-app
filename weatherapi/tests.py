from rest_framework import status
from rest_framework.test import APITestCase


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

    def test_get_weather(self):
        response = self.client.get('/api/locations/maputo?days=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
