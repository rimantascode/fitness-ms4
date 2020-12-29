from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    CustomerIdstripe = models.CharField(max_length=255)
    SubscriptionIdstripe = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
