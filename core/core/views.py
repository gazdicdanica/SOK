import operator
from typing import List
from django.apps.registry import apps
from django.shortcuts import render
 
from .services.parse import DataParserBase
from .services.model import Node, Edge, Graph, ATTR_ID
 
 
 
 
def index(request):
    parse_plugins: List[DataParserBase] = apps.get_app_config('core').parse_plugins
    render_plugins: List[DataParserBase] = apps.get_app_config('core').render_plugins
    print("Parse Plugins: " + ", ".join(plugin.name() for plugin in parse_plugins))
    print("Render Plugins: " + ", ".join(plugin.name() for plugin in render_plugins))
 
    test_graph()
    test_filter()
 
    for parse_plugin in parse_plugins:
        if parse_plugin.name() == "YAMLParser":
            test_YAML_parse(parse_plugin)
        elif parse_plugin.name() == "JSONParser":
            test_JSON_parse(parse_plugin)
 
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
 
 
def test_YAML_parse(parser: DataParserBase):
    test_string = """
---
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
  - *cvor6
"""
 
    print(parser)
    graph = parser.parse(test_string)
 
    for n in graph.nodes:
        if n.has_attr(ATTR_ID):
            print(n.get_attr(ATTR_ID) + " " + str(n.attr))
 
    for e in graph.edges:
        if e.node_from.has_attr(ATTR_ID) and e.node_to.has_attr(ATTR_ID):
            print(e.node_from.get_attr(ATTR_ID) + " -> " + e.node_to.get_attr(ATTR_ID))
        else:
            print(str(e.node_from.attr) + " -> " + str(e.node_to.attr))
 
    print("=============================================")
 
 
def test_JSON_parse(parser: DataParserBase):
    test_string = """
{
    "name": "ROOT",
    "data":[
        {
            "__id":"1",
            "name":"cvor1",
            "miniNodes":[
                {
                    "__id":"5",
                    "timestamp": "12:40:34",
                    "name":"miniCvor1",
                    "__ref":["1","6", "7"]
                }
            ]
        },
        {
            "__id":"2",
            "name":"cvor2"
        },
        {
            "__id":"3",
            "name":"cvor3",
            "miniNodes":[
                {
                    "__id":"6",
                    "date": "01-01-2000",
                    "name":"miniCvor2",
                    "__ref":["4"],
                    "randomInfo": ["info1", "info2"]
                },
                {
                    "__id":"7",
                    "name":"miniCvor3",
                    "timestamp": "10:30:10",
                    "miniMiniNodes":[
                        {
                            "__id":"9",
                            "name":"miniMiniCvor1",
                            "__ref":["3"]
                        }
                    ]
                }
            ]
        },
        {
            "__id":"4",
            "name":"cvor4",
            "date": "01-01-2001",
            "miniNodes":[
                {
                    "__id":"8",
                    "name":"miniCvor4",
                    "__ref":["1", "3"]
                }
            ]
        }
    ]
}
    """
 
    print(parser)
    graph = parser.parse(test_string)
 
    for n in graph.nodes:
        if n.has_attr(ATTR_ID):
            print(n.get_attr(ATTR_ID) + " " + str(n.attr))
 
    for e in graph.edges:
        if e.node_from.has_attr(ATTR_ID) and e.node_to.has_attr(ATTR_ID):
            print(e.node_from.get_attr(ATTR_ID) + " -> " + e.node_to.get_attr(ATTR_ID))
        else:
            print(str(e.node_from.attr) + " -> " + str(e.node_to.attr))
 
    print("=============================================")
 
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
 