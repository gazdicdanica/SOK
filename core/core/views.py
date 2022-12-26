import operator
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
    test_filter()

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


def test_filter():
    vertices = []
    for i in range(10):
        vertex = Node()
        vertex.attr = {"val": i}
        vertices.append(vertex)

    edges = []
    for i in range(4, 7):
        edge = Edge(vertices[i], vertices[i - 1])
        edge.attr = {"val": i}
        edges.append(edge)

    graph_1 = Graph(vertices, edges)
    graph_1_filtered = graph_1.filter("val", "5", operator.ge, True, True)
    graph_2_filtered = graph_1.filter("val", "5", operator.ge, False, True)
    graph_3_filtered = graph_1.filter("val", "5", operator.ge, True, False)
    graph_4_filtered = graph_1.filter("v", "5", operator.ge, True, True)
    graph_5_filtered = graph_1.filter("val", "5", operator.ge, False, True).filter("val", "5", operator.ge, True, False)
    graphs =[]
    graphs.append(graph_1_filtered)
    graphs.append(graph_2_filtered)
    graphs.append(graph_3_filtered)
    graphs.append(graph_4_filtered)
    graphs.append(graph_5_filtered)

    for graph in graphs:
        print("Vertices")
        for vertex in graph.nodes:
            print(vertex.attr)
        print("Edges")
        for edge in graph.edges:
            print(edge.attr)
        print()