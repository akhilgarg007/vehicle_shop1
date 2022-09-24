from django.contrib.auth import get_user_model

from rest_framework import serializers as rest_serializers

from user import models as user_models
from vehicles import serializers as vehicles_serializer


User = get_user_model()


class AddressSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer to serialize address, overriden to make all the fields as required
    """
    class Meta:
        model = user_models.Address
        fields = ('number', 'street', 'city', 'country')
        extra_kwargs = {
            'number': {'required': True},
            'street': {'required': True},
            'city': {'required': True},
            'country': {'required': True},
        }


class UserSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer to serialize user for create user api
    """
    cars = vehicles_serializer.CarSerializer(many=True, required=True)
    address = AddressSerializer(required=True)

    class Meta:
        model = User
        fields = ('age', 'username', 'first_name', 'last_name', 'email', 'cars', 'address')
        extra_kwargs = {
            'age': {'required': True}
        }

    def validate(self, data):
        """
        Check that at least 1 car is present while creating user
        """
        if not data['cars']:
            raise rest_serializers.ValidationError('At least 1 car is required.')
        return data


class UpdateUserSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer to update user and his address
    """
    address = AddressSerializer(required=True)

    class Meta:
        model = User
        fields = ('age', 'username', 'first_name', 'last_name', 'email', 'address')

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        for key, value in address_data.items():
            setattr(instance.address, key, value)
        instance.address.save()
        return super().update(instance, validated_data)


class UserNameSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer for user first name and last name
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
