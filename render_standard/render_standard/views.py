from django.http import HttpResponse
from core.services.render_standard import RendererStandard

def index(request):
    return HttpResponse(f"Hello from {RendererStandard().name()}")