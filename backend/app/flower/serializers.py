from rest_framework import serializers


class FlowerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    color = serializers.CharField(max_length=30)
