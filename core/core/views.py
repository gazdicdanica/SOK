from typing import List
from django.apps.registry import apps
from django.shortcuts import render

from .services.parse import DataParserBase
from .services.model import Node, Edge, Graph


def index(request):
    parse_plugins: List[DataParserBase] = apps.get_app_config('core').parse_plugins
    render_plugins: List[DataParserBase] = apps.get_app_config('core').render_plugins
    print("Parse Plugins: " + ", ".join(plugin.name() for plugin in parse_plugins))
    print("Render Plugins: " + ", ".join(plugin.name() for plugin in render_plugins))

    test_graph()

    return render(request, "hello_world.html")


def test_graph():
    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()

    e1 = Edge(n1, n2)
    e2 = Edge(n1, n3)
    e3 = Edge(n2, n3)
    e4 = Edge(n4, n1)
    e5 = Edge(n4, n3)

    nodes = [n1, n2, n3, n4]
    edges = [e1, e2, e3, e4, e5]

    g = Graph(nodes, edges)

    print(len(g.nodes))
    for n in g.nodes:
        print(n)

    print(len(g.edges))
    for e in g.edges:
        print(e)