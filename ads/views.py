from rest_framework import viewsets as rest_viewsets

from ads import (
    models as ads_models,
    serializers as ads_serializers
)


class AdViewSet(rest_viewsets.ModelViewSet):
    """
    Viewset for create, update and delete and view ads
    """
    create_update_serializer_class = ads_serializers.CreateUpdateAdsSerializer
    serializer_class = ads_serializers.AdsSerializer
    queryset = ads_models.Ads.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_class if self.request.method == 'GET' else self.create_update_serializer_class

