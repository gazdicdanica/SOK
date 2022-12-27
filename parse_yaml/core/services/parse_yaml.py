import yaml
from core.services.parse import DataParserBase
from core.services.model import *


class YAMLParser(DataParserBase):
    def identifier(self) -> str:
        return "#YAMLParser"


    def name(self) -> str:
        return "YAMLParser"


    def parse(self, data: str) -> None:
        return None


    def parseFile(self, fname: str) -> dict:
        print(fname)
        with open(fname, 'r') as file:
            dataMap = yaml.safe_load(file)
        return dataMap


    def processParsedData(self, data, parent_node: Node, graph: Graph):
        node = Node()
        for key in data:
            if type(data[key]) is list:
                if key != ATTR_REF:
                    if(all(type(n) is dict for n in data[key])):
                        for child_node in data[key]:
                            self.processParsedData(child_node, node, graph)
                    else:
                        node.attr[key] = data[key]
            elif type(data[key]) is dict:
                self.processParsedData(data[key], node, graph)
            else:
                node.attr[key] = data[key]

        # connecting children to parent node
        self.connectNodes(graph, node, parent_node)

        if ATTR_REF in data:
            self.connectByRef(graph, node, data[ATTR_REF])
        

    def connectByRef(self, graph: Graph, node: Node, references):
        for ref in references:
            for n in graph.nodes:
                if n.get_attr(ATTR_ID) == ref[ATTR_ID]:
                    edge = Edge(node, n)
                    graph.edges.append(edge)



    def connectNodes(self, graph: Graph, child_node: Node, parent_node: Node):
        if parent_node:
            edge = Edge(parent_node, child_node)
            graph.edges.append(edge)

        graph.nodes.append(child_node)


    def generateGraph(self) -> Graph:
        graph = Graph([], [])

        data = self.parseFile("./data/test.yml")

        data = self.parseFile("./data/cyclic_graph.yml")

        self.processParsedData(data, None, graph)
      