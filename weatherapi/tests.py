from django.test import TestCase

# Create your tests here.
from rest_framework.exceptions import APIException
from rest_framework.test import APIRequestFactory


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'
