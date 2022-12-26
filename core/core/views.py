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


def tests(request):
    results = test_search()
    context = {"test_results": results}
    return render(request, "tests.html", context)


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


def test_search():
    results = []

    nodes = []
    edges = []
    for i in range(4):
        nodes.append(Node())

    edges.append(Edge(nodes[0], nodes[1]))
    edges.append(Edge(nodes[1], nodes[2]))
    edges.append(Edge(nodes[2], nodes[3]))

    g = Graph(nodes, edges)
    g.nodes[0]["name"] = "Perica"
    g.nodes[1]["name"] = "Ivica"
    g.nodes[2]["name"] = "Per"

    g.edges[0]["name"] = "per"
    g.edges[1]["asd"] = "adw"

    sg = g.search("per", True, True)
    results.append(print_case(len(sg.nodes) == 2, 1))
    results.append(print_case(len(sg.edges) == 1, 2))

    sg = g.search("per", True, False)
    results.append(print_case(len(sg.nodes) == 4, 3))
    results.append(print_case(len(sg.edges) == 3, 4))

    sg = g.search("per", False, True)
    results.append(print_case(len(sg.nodes) == 2, 5))
    results.append(print_case(len(sg.edges) == 1, 6))

    sg = g.search("per", False, False)
    results.append(print_case(len(sg.nodes) == 4, 7))
    results.append(print_case(len(sg.edges) == 3, 8))

    sg = g.search("ivica", True, False)
    results.append(print_case(len(sg.nodes) == 3, 9))
    results.append(print_case(len(sg.edges) == 2, 10))
    return results


def print_case(val, serial):
    if val:
        return "{0} Passed\r\n".format(serial)
    else:
        return "{0} Failed\r\n".format(serial)


