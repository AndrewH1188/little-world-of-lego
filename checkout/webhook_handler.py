from django.http import HttpResponse

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project

class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)