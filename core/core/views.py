from typing import List
from django.apps.registry import apps
from django.shortcuts import render

from .services.parse import DataParserBase

def index(request):
    parse_plugins: List[DataParserBase] = apps.get_app_config('core').parse_plugins
    render_plugins: List[DataParserBase] = apps.get_app_config('core').render_plugins
    print("Parse Plugins: " + ", ".join(plugin.name() for plugin in parse_plugins))
    print("Render Plugins: " + ", ".join(plugin.name() for plugin in render_plugins))

    return render(request, "hello_world.html")