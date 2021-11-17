from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """The weather result serializer, define your fields here."""
    maximum = serializers.IntegerField()
    minimum = serializers.IntegerField()
    average = serializers.IntegerField()
    median = serializers.IntegerField()

