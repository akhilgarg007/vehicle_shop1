from django.contrib.auth import get_user_model
from django.db import models

from vehicles import models as vehicles_models

User = get_user_model()


class Ads(models.Model):
    """
    Model to store ads
    """
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='ads', max_length=511)
    users = models.ManyToManyField(User)
    car = models.ForeignKey(vehicles_models.Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}->{self.description}->{self.price_per_km}'
