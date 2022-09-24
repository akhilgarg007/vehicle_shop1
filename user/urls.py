from django.urls import path

from user import views as user_views

urlpatterns = [
    path('create/', user_views.CreateUserView.as_view(), name='create_user'),
    path('update/<int:pk>/', user_views.UpdateUserView.as_view(), name='update_user'),
]
