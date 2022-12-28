import json

from core.services.parse import DataParserBase

from core.services.model import *


def loadData(fname: str):
    print(fname)
    with open(fname, 'rt', buffering=100000) as fn:
        data = fn.read()
    return json.loads(data)


class JSONParser(DataParserBase):
    def identifier(self) -> str:
        return "#JSONParser"

    def name(self) -> str:
        return "JSONParser"

    def parse(self, data: str) -> Graph:
        graph = Graph([], [])

        self._processParsedData(json.loads(data), graph)

        return graph

    def parseFile(self, fname: str) -> Graph:
        graph = Graph([], [])

        self._processParsedData(loadData(fname), graph)

        return graph

    def _processParsedData(self, data, graph: Graph, parent_node: Node = None):
        node = Node()
        for key in data:
            if isinstance(data[key], dict):
                self._processParsedData(data[key], graph, node)
            elif isinstance(data[key], list):
                if all(type(n) is dict for n in data[key]):
                    for child_node in data[key]:
                        self._processParsedData(child_node, graph, node)
                else:
                    node.attr[key] = data[key]
            else:
                node.attr[key] = data[key]

        self._connectNodes(graph, node, parent_node)
        if ATTR_REF in data:
            self._connectByRef(graph, node, data[ATTR_REF])

    def _connectByRef(self, graph: Graph, node: Node, references):
        for id in references:
            reference_node = None
            for n in graph.nodes:
                # is the node already added to graph?
                if n.get_attr(ATTR_ID) == id:
                    reference_node = n
                    break
            # generate new node if it isn't
            if reference_node is None:
                reference_node = Node()
                reference_node.attr[ATTR_ID] = id
                graph.nodes.append(reference_node)

            edge = Edge(node, reference_node)
            graph.edges.append(edge)

    def _connectNodes(self, graph: Graph, node: Node, parent_node: Node):
        if parent_node:
            edge = Edge(parent_node, node)
            graph.edges.append(edge)

        if node.has_attr(ATTR_ID):
            li = [x for x in graph.nodes if x.get_attr(ATTR_ID) == node.get_attr(ATTR_ID)]
            if li:
                for key in node.attr:
                    li[0].attr[key] = node.attr[key]
            else:
                graph.nodes.append(node)
        else:
            graph.nodes.append(node)
