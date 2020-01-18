from rest_framework import serializers
from .models import Flower, Bunch


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ('name', 'color', 'quantity')


class BunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bunch
        fields = '__all__'
