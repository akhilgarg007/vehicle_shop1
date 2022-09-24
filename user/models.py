from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    """
    Model to store address of user. Creating as a separate model as we may have shops added in the future and they may
    also have address
    """
    number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.number}->{self.street}->{self.city}->{self.country}'


class User(AbstractUser):
    """
    Overridden user model to add age and address
    """
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
