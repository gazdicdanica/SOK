from typing import List
from django.apps.registry import apps
from django.shortcuts import render

from .services.parse import DataParserBase
from .services.model import Node, Edge, Graph, ATTR_ID
from parse_yaml.core.services.parse_yaml import YAMLParser


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


def test_YAML_parse():
    test_string = """---
        name: ROOT
        data:
        - &cvor1
        __id: '1'
        name: cvor1
        miniNodes:
        - __id: '5'
            timestamp: '12:40:34'
            name: miniCvor1
            __ref:
            - *cvor1
        - __id: '2'
        name: cvor2
        - &cvor3
        __id: '3'
        name: cvor3
        miniNodes:
        - &cvor6
            __id: '6'
            date: 01-01-2000
            name: miniCvor2
            randomInfo:
            - info1
            - info2
        - __id: '7'
            name: miniCvor3
            timestamp: '10:30:10'
            miniMiniNodes:
            - __id: '9'
            name: miniMiniCvor1
            __ref:
            - *cvor3
        - __id: '4'
        name: cvor4
        date: 01-01-2001
        miniNodes:
        - __id: '8'
            name: miniCvor4
            __ref:
            - *cvor1
            - *cvor3
        __ref:
        - *cvor6"""
        
    parser = YAMLParser()
    graph = parser.parse(test_string)

    for n in graph.nodes:
        if n.has_attr(ATTR_ID):
            print(n.get_attr(ATTR_ID) + " " + str(n.attr))

    for e in graph.edges:
        if e.node_from.has_attr(ATTR_ID) and e.node_to.has_attr(ATTR_ID):
            print(e.node_from.get_attr(ATTR_ID) + " " + e.node_to.get_attr(ATTR_ID))
        else:
            print(str(e.node_from.attr) + " -> " + str(e.node_to.attr))