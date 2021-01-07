from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from subscription_plans.models import Subscriptions, exercisesPlan
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from dateutil.relativedelta import relativedelta

from datetime import date
import stripe

def check_subscription(request):
    try:
        stripe_customer = Subscriptions.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.SubscriptionIdstripe)
        product = stripe.Product.retrieve(subscription.plan.product)
        expire_date = stripe_customer.expire_date

        if subscription.status == "active":
            a = "handshake"
            return a
        else:
            a = "no"
      
    except Subscriptions.DoesNotExist:
       messages.error(request, "Sorry, only subscribed users can access this service")


@login_required
def subscription_plans(request):
    try:
        stripe_customer = Subscriptions.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.SubscriptionIdstripe)
        product = stripe.Product.retrieve(subscription.plan.product)
        expire_date=stripe_customer.expire_date

        context = {
                'subscription': subscription,
                'product': product,
                'expire_date': expire_date
        }
       
        return render(request, 'subscription_plans/subscription_plans.html', context)
        
    except Subscriptions.DoesNotExist:
        return render(request, 'subscription_plans/subscription_plans.html')

    return render(request, 'subscription_plans/subscription_plans.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        STRIPE_PRICE_ID = settings.STRIPE_PRICE_ID
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url +
                'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': "price_1I3S3cA3o7Dh28QGEfwpxFAG",
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            messages.error(request, f'{str(e)}')
            return JsonResponse({'error': str(e)})
            


@login_required
def success(request):
    try:
        stripe_customer = Subscriptions.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.SubscriptionIdstripe)
        product = stripe.Product.retrieve(subscription.plan.product)
        expire_date = stripe_customer.expire_date

        context = {
            'subscription': subscription,
            'product': product,
            'expire_date': expire_date
        }
        messages.success(
            request, "you have successfully subscribed, and now you granted to access the exercises and nutrition plans")
        return redirect(reverse('subscription_plans'))

    except Subscriptions.DoesNotExist:
        messages.error(
            request, "sorry something went wrong!!!!")
        return redirect(reverse('subscription_plans'))

    return redirect(reverse('subscription_plans'))
   


@login_required
def declined(request):
    return render(request, 'subscription_plans/cancel.html')


@require_POST
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_SUB_WEBHOOK
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
        
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session2 = event
    
        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')
        stripe_subscription_created = session2.get('created')
        theDateOfSubscription = date.fromtimestamp(stripe_subscription_created)
        expire_date = theDateOfSubscription + relativedelta(months=+3)
        
        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        Subscriptions.objects.create(
            user=user,
            CustomerIdstripe=stripe_customer_id,
            SubscriptionIdstripe=stripe_subscription_id,
            subscription_date = theDateOfSubscription,
            expire_date = expire_date)
        
        messages.success(request, "You have successuly subscribed")
       
    return HttpResponse(status=200)


@login_required
def all_exercises_plans(request):
    try:
        exercises = exercisesPlan.objects.all()
        stripe_customer = Subscriptions.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(
            stripe_customer.SubscriptionIdstripe)
        product = stripe.Product.retrieve(subscription.plan.product)
        expire_date = stripe_customer.expire_date

        context = {
            'subscription': subscription,
            'product': product,
            'expire_date': expire_date,
            'exercises':  exercises
        }

        return render(request, 'subscription_plans/exercises_plans.html', context)

    except Subscriptions.DoesNotExist:
        return redirect(reverse('subscription_plans'))

    return render(request, 'subscription_plans/subscription_plans.html')

def exercise_details(request,  exercise_id):
    exercise_details = get_object_or_404(exercisesPlan, pk=exercise_id)
    
    context={
        'exercise_details':exercise_details,
        'subscription':  check_subscription(request)
    }
    return render(request, "subscription_plans/exercise_details.html", context)
