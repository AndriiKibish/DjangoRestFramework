from carsapi.models import Car
from rest_framework import serializers


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
