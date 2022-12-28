from django.http import HttpResponse
from core.services.render_classdiag import RendererClassDiagram

def index(request):
    return HttpResponse(f"Hello from {RendererClassDiagram().name()}")