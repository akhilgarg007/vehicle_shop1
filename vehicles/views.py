from rest_framework import generics as rest_generics

from vehicles import (
    models as vehicles_models,
    serializers as vehicles_serializers
)


class UpdateCarView(rest_generics.UpdateAPIView):
    """
    View to update user and his address
    """
    serializer_class = vehicles_serializers.CarSerializer
    queryset = vehicles_models.Car.objects.all()
