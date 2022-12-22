from django.http import HttpResponse
from core.services.render3 import Renderer3


def index(request):
    return HttpResponse(f"Hello from {Renderer3().name()}")