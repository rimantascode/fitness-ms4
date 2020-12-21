from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51I0jWJA3o7Dh28QGfwFw9XqG9jpTEAm5o7TTgSWzrmqhel4gToXE8LymGb9GhSoRHjrmufpJeR3e1nbinXjV61dZ00Vn7K8bza',
        'client_secret':'client secret test',


    }

    return render(request, template, context)
