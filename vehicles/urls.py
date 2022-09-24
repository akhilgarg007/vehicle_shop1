from django.urls import path

from vehicles import views as vehicles_views

urlpatterns = [
    path('update/<int:pk>/', vehicles_views.UpdateCarView.as_view(), name='update_car'),
]
