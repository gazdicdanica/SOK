import yaml
from core.services.parse import DataParserBase
from core.services.model import *


class YAMLParser(DataParserBase):
    def identifier(self) -> str:
        return "#YAMLParser"


    def name(self) -> str:
        return "YAMLParser"


    def parse(self, data: str) -> Graph:
        dataMap = yaml.safe_load(data)
        graph = Graph([], [])

        self.processParsedData(dataMap, None, graph)

        return graph


    def parseFile(self, fname: str) -> None:
        print(fname)
        with open(fname, 'r') as file:
            data = file.read()
        self.parse(data)
            


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
            referenceNode = None
            for n in graph.nodes:
                # is the node already added to graph?
                if n.get_attr(ATTR_ID) == ref[ATTR_ID]:
                    referenceNode = n
                    break
            # generate new node if it isn't
            if referenceNode is None:
                referenceNode = Node()
                referenceNode.attr[ATTR_ID] = ref[ATTR_ID]
                graph.nodes.append(referenceNode)
            
            edge = Edge(node, referenceNode)
            graph.edges.append(edge)


    def connectNodes(self, graph: Graph, child_node: Node, parent_node: Node):
        if parent_node:
            edge = Edge(parent_node, child_node)
            graph.edges.append(edge)


        if child_node.has_attr(ATTR_ID):
            li = [x for x in graph.nodes if x.get_attr(ATTR_ID) == child_node.get_attr(ATTR_ID)]
            if li:
               for key in child_node.attr:
                li[0].attr[key] = child_node.attr[key]
            else:
                graph.nodes.append(child_node)
        else: 
            graph.nodes.append(child_node)

