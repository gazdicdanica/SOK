import operator
from typing import List, Dict, Any, Callable, Tuple
from operator import lt, le, gt, ge, eq, ne

ATTR_ID = "__id"
ATTR_REF = "__ref"


class Node:
    def __init__(self):
        self._attr = {}

    @property
    def attr(self) -> Dict:
        return self._attr

    @attr.setter
    def attr(self, newval: Dict):
        self._attr = newval

    def has_attr(self, attr_name: str) -> bool:
        return attr_name in self.attr

    def get_attr(self, attr_name: str) -> Any:
        """
            Desc:
                Returns the attribute of this node.
                Shorthand for attr[attr_name].
                
            Note:
                This function does not perform an existence check.
                on the specified attribute.
        """
        return self.attr[attr_name]

    def search(self, query: str) -> List[str]:
        """
            Desc:
                Perform text search on this node.
            
            Note:
                Searching should be done with substrings.

            Args:
                query: str - the text query to search for.

            Returns:
                A list of attribute names of this node whose values satisfy the search.
                or an empty list if none found.
        """

        # TODO: Needs implementation
        return []

    def query_check(self, attr_name: str, val: str, operator: Callable[[Any, Any], bool]) -> bool:
        """
            Desc:
                Perform attribute query on the node's attribute.

            Args:
                attr_name: str - Name of the attribute.
                val: str - Expected value.
                operator: (any, any) -> (bool) - Binary operator to apply to the values.
                    Expected values: operator.lt, operator.gt, operator.ge, operator.le, operator.eq, operator.ne

            Returns:
                False if this node doesn't have the attribute `attr_name`.
                True if operator(attr[attr_name], val) is True.
                False otherwise.

            Throws:
                NotImplementedError if the type of `val` isn't supported.
        """
        try:
            attribute = self.get_attr(attr_name)
        except:
            return False
        try:
            return operator(attribute, type(self.get_attr(attr_name))(val))
        except:
            raise NotImplementedError("value type not supported")


class Edge:
    def __init__(self, node1: Node, node2: Node):
        self._attr = {}
        self._node_from = node1
        self._node_to = node2

    @property
    def attr(self) -> Dict:
        return self._attr

    @attr.setter
    def attr(self, newval: Dict):
        self._attr = newval

    @property
    def node_from(self) -> Node:
        return self._node_from

    @node_from.setter
    def node_from(self, newval: Node):
        self._node_from = newval

    @property
    def node_to(self) -> Node:
        return self._node_to

    @node_to.setter
    def node_to(self, newval: Node):
        self._node_to = newval

    def get_attr(self, attr_name: str) -> Any:
        """
            Desc:
                Returns the attribute of this node.
                Shorthand for attr[attr_name].

            Note:
                This function does not perform an existence check.
                on the specified attribute.
        """
        return self.attr[attr_name]

    def query_check(self, attr_name: str, val: str, operator: Callable[[Any, Any], bool]) -> bool:
        """
            Desc:
                Perform attribute query on the edge.

            Args:
                attr_name: str - Name of the attribute.
                val: str - Expected value.
                operator: (any, any) -> (bool) - Binary operator to apply to the values.
                    Expected values: operator.lt, operator.gt, operator.ge, operator.le, operator.eq, operator.ne

            Returns:
                True if query_check returns True for both of the nodes of this edge.
                False othewise.

            Throws:
                NotImplementedError if the type of `val` isn't supported (see query_check).
        """
        try:
            attribute = self.get_attr(attr_name)
        except:
            return False
        try:
            return operator(attribute, type(self.get_attr(attr_name))(val))
        except:
            raise NotImplementedError("value type not supported")


class Graph:
    def __init__(self, nodes: List[Node], edges: List[Edge]):
        self._nodes = nodes
        self._edges = edges

    def clear(self) -> None:
        self._nodes = []
        self._edges = []

    def search(self, query: str) -> "Graph":
        """
            Desc:
                Perform search under the whole graph.

            Args:
                query: str - the text query to search for.

            Returns:
                A subgraph (Graph) whose elements are
                nodes which satisfy the search with given
                search query.
        """

        # TODO: Implementation needed.

        return []

    def filter(self, attr_name: str, val: str, operator: Callable[[Any, Any], bool], by_vertices: bool,
               by_edges: bool) -> "Graph":
        """
            Desc:
                Perform graph filtering using a query expression.

            Args:
                attr_name: str - Name of the attribute.
                val: str - Expected value.
                operator: (any, any) -> (bool) - Binary operator to apply to the values.
                    Expected values: operator.lt, operator.gt, operator.ge, operator.le, operator.eq, operator.ne

            Returns:
                A Graph instance whose nodes and edges all satisfy the filter.
                Empty graph if no such nodes found.

            Note:
                This method must NOT modify the calling graph instance.

            Throws:
                NotImplementedError if the type of `val` isn't supported (see query_check).       
        """

        if len(self._nodes) == 0:
            return Graph([], [])

        passed_vertices = self.filter_vertices(attr_name, operator, val) \
            if by_vertices else self._nodes

        if len(passed_vertices) == 0:
            return Graph([], [])

        passed_edges = self.filter_edges(attr_name, operator, passed_vertices, val) \
            if by_edges else self.check_connecting_vertices(self._edges, passed_vertices)

        return Graph(passed_vertices, passed_edges)

    def filter_edges(self, attr_name, operator, passed_vertices, val):
        passed_edges = []
        for edge in self._edges:
            if edge.query_check(attr_name, val, operator):
                if operator(type(val)(edge.get_attr(attr_name)), val):
                    passed_edges.append(edge)

        return self.check_connecting_vertices(passed_edges, passed_vertices)

    def check_connecting_vertices(self, edges, passed_vertices):
        passed_edges = []
        for edge in edges:
            if edge.node_to in passed_vertices and edge.node_from in passed_vertices:
                passed_edges.append(edge)
        return passed_edges

    def filter_vertices(self, attr_name, operator, val):
        passed_vertices = []
        for vertex in self._nodes:
            if vertex.query_check(attr_name, val, operator):
                if operator(type(val)(vertex.get_attr(attr_name)), val):
                    passed_vertices.append(vertex)
        return passed_vertices

    @property
    def nodes(self) -> List[Node]:
        return self._nodes

    @nodes.setter
    def nodes(self, newval: List[Node]):
        self._nodes = newval

    @property
    def edges(self) -> List[Edge]:
        return self._edges

    @edges.setter
    def edges(self, newval: List[Edge]):
        self._edges = newval


if __name__ == "__main__":
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
    graphs.append(graph_5_filtered)
    graphs.append(graph_4_filtered)
    graphs.append(graph_3_filtered)
    graphs.append(graph_2_filtered)
    graphs.append(graph_1_filtered)

    for graph in graphs:
        for vertex in graph.nodes:
            print(vertex.attr)

        for edge in graph.edges:
            print(edge.attr)
