from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class WeatherTests(APITestCase):
    def test_method_not_allowed(self):
        response = self.client.post('/api/locations/maputo')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_resource_not_found(self):
        response = self.client.post('/api/locations/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
