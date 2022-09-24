from django.contrib.auth import get_user_model

from rest_framework import (
    generics as rest_generics,
    response as rest_response,
    status as rest_status,
)

from user import (
    models as user_models,
    serializers as user_serializers
)
from vehicles import models as vehicles_models


User = get_user_model()


class CreateUserView(rest_generics.CreateAPIView):
    """
    View to create user, address and cars
    """
    serializer_class = user_serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return rest_response.Response({'success': False}, status=rest_status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        cars = validated_data.pop('cars')
        address = validated_data.pop('address')
        address = user_models.Address.objects.create(**address)
        user = User.objects.create(**validated_data, address=address)
        for car in cars:
            vehicles_models.Car.objects.create(**car, user=user)
        return rest_response.Response({'success': True}, status=rest_status.HTTP_201_CREATED)


class UpdateUserView(rest_generics.UpdateAPIView):
    """
    View to update user and his address
    """
    serializer_class = user_serializers.UpdateUserSerializer
    queryset = User.objects.all()
