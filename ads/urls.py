from rest_framework import routers as rest_routers

from ads import views as ads_views

router = rest_routers.SimpleRouter()

router.register('', ads_views.AdViewSet, 'ads')

urlpatterns = router.urls
