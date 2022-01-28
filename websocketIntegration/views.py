from django.http import HttpResponse
from websocketIntegration.signals import update_signal


def index(request):
    update_signal.send('', msg='I was wondering if after all these years you\'d like to meet')
    return HttpResponse("Hello, it\'s me...")
