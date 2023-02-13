import datetime
import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from stripe.api_resources import event

from .models import Payment, PaymentHistory

stripe.api_key = settings.STRIPE_SECRET_KEY
endpoint_secret = 'whsec_1b94fd11575653244748ac613d98c47814962ab2d69424f4f0eff6d1a47eb51a'


# Create your views here.
class CreateCheckoutSessionView(APIView):
    def post(self, request, *args, **kwargs):
        payment = Payment.objects.get(pk=self.kwargs['pk'])
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
            metadata={
                'payment_id': payment.id
            },
            mode='payment',
            success_url="http://localhost:3000" + '/success/',
            cancel_url="http://127.0.0.1:8000" + '/cancel/',
        )
        return redirect(checkout_session.url)


@csrf_exempt
def my_webhook_view(request):
    payload = request.body
    decoded_payload = json.loads(payload.decode('utf-8'))
    event = None
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
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

    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
            event['data']['object']['id'],
            expand=['line_items'],
        )
        print(session.payment_method_types[0])
        payment = Payment.objects.get(id= session.metadata.payment_id)
        PaymentHistory.objects.create(
            user=payment.user,
            amount_paid=session.line_items.data[0].amount_total,
            payment_method=session.payment_method_types[0],
            at=datetime.datetime.now()
        )
        print(session)
        # Passed signature verification
    return HttpResponse(status=200)
