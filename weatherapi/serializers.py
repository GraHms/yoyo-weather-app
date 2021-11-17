from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """The weather result serializer, define your fields here."""
    maximum = serializers.FloatField()
    minimum = serializers.FloatField()
    average = serializers.FloatField()
    median = serializers.FloatField()

