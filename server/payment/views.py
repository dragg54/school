import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
class CreateCheckoutSessionView(APIView):
    def post(self, request, *args, **kwargs):
        payment = Payment.objects.get(pk=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(payment.amount_payable) * 100,
                    'product_data': {

                        'name': payment.name
                    }
                },
                    'quantity': 1
                }

            ],
            mode='payment',
            success_url="http://127.0.0.1:8000" + '/success/',
            cancel_url="http://127.0.0.1:8000" + '/cancel/',
        )
        return redirect(checkout_session.url)
