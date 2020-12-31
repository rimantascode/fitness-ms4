from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_plans,
         name='subscription_plans'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),  
    path('cancel/', views.declined, name="declined"), 
    path('exercises_plans/', views.all_exercises_plans, name="all_exercises_plans"),
    path('exercise_details/<int:exercise_id>/', views.exercise_details,
         name="exercise_details"),
    path('webhook/', views.stripe_webhook)
]
