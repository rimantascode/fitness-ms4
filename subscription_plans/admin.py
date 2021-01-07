from django.contrib import admin


from django.contrib import admin
from subscription_plans.models import Subscriptions, exercisesPlan


admin.site.register(Subscriptions)
admin.site.register(exercisesPlan)
