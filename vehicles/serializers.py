from rest_framework import serializers as rest_serializers

from vehicles import models as vehicles_models


class CarSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer to serializer car
    """

    class Meta:
        model = vehicles_models.Car
        fields = ('number_plate', 'model', 'brand')
        extra_kwargs = {
            'number_plate': {'required': True},
            'model': {'required': True},
            'brand': {'required': True},
        }

