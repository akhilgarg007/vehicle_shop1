from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Car(models.Model):
    """
    Model to store car belonging to user
    """
    number_plate = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}->{self.brand}->{self.model}->{self.number_plate}'
