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