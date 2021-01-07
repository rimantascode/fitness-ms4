from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save


class Subscriptions(models.Model):
    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
    CustomerIdstripe = models.CharField(max_length=255)
    SubscriptionIdstripe = models.CharField(max_length=255)
    expire_date = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    subscription_date = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.user.username


class exercisesPlan(models.Model):
    how_it_works = models.TextField(max_length=2000, blank=True)
    hero_image = models.URLField(
        max_length=1400, null=True, blank=True)

    name = models.CharField(max_length=100, blank=False)

    rating = models.DecimalField(max_digits=6, decimal_places=2)

    directions = models.TextField(max_length=2000, blank=False)

    day_1 = models.CharField(max_length=200, blank=True, null=True)
    source_1 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_1 = models.TextField(max_length=2000, blank=True)

    day_2 = models.CharField(max_length=200, blank=True, null=True)
    source_2 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_2 = models.TextField(max_length=2000, blank=True)

    day_3 = models.CharField(max_length=200, blank=True, null=True)
    source_3 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_3 = models.TextField(max_length=2000, blank=True)

    day_4 = models.CharField(max_length=200, blank=True, null=True)
    source_4 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_4 = models.TextField(max_length=2000, blank=True)

    day_5 = models.CharField(max_length=200, blank=True, null=True)
    source_5 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_5 = models.TextField(max_length=2000, blank=True)

    day_6 = models.CharField(max_length=200, blank=True, null=True)
    source_6 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_6 = models.TextField(max_length=2000, blank=True)

    day_7 = models.CharField(max_length=200, blank=True, null=True)
    source_7 = models.TextField(
        max_length=1400, null=True, blank=True)
    description_7 = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name
