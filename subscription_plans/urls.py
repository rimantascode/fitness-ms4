from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans,
         name='subscription_plans'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),  
    path('cancel/', views.declined),  
    path('webhook/', views.stripe_webhook)
]
