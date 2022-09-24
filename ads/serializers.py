from django.contrib.auth import get_user_model

from rest_framework import serializers as rest_serializers

from ads import models as ads_models
from user import serializers as user_serializers
from vehicles import serializers as vehicles_serializers

User = get_user_model()


class AdsSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer to serialize ad
    """
    users = user_serializers.UserNameSerializer(many=True, required=False)
    car = vehicles_serializers.CarSerializer(required=False)

    class Meta:
        model = ads_models.Ads
        fields = ('created_at', 'title', 'description', 'price_per_km', 'image', 'users', 'car')
        extra_kwargs = {
            'created_at': {'read_only': True},
        }


class CreateUpdateAdsSerializer(rest_serializers.ModelSerializer):
    """
    Custom serializer to serialize ad input and update
    """

    class Meta:
        model = ads_models.Ads
        fields = ('title', 'description', 'price_per_km', 'image', 'users', 'car')
        extra_kwargs = {
            'image': {'required': False}
        }
