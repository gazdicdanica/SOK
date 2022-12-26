from typing import List, Dict, Any, Callable, Tuple
from operator import lt, le, gt, ge, eq, ne

ATTR_ID = "__id"
ATTR_REF = "__ref"


class Attributable(object):
    def __init__(self):
        self._attr = {}

    @property
    def attr(self) -> Dict:
        return self._attr

    @attr.setter
    def attr(self, newval: Dict):
        self._attr = newval

    def set_attr(self, attr_name: str, val: Any):
        self._attr[attr_name] = val

    def has_attr(self, attr_name: str) -> bool:
        return attr_name in self.attr

    def satisfies_query(self, query: str):
        return len(self.search(query)) != 0

    def get_attr(self, attr_name: str) -> Any:
        """
            Desc:
                Returns the attribute of this node.
                Shorthand for attr[attr_name].

            Note:
                This function does not perform an existence check.
                on the specified attribute.
        """
        return self.attr.get(attr_name)

    def __getitem__(self, key):
        return self._attr.get(key)

    def __setitem__(self, key, value):
        self._attr[key] = value

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
        return [attr_name for attr_name in self.attr if query.lower() in str(self.get_attr(attr_name)).lower()]

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

        # TODO: Needs implementation
        # TODO: Manual conversion after get_attr (int, float, bool, str)
        # TODO: return operator(my value, val converted)
        return False


class Node(Attributable):
    def __init__(self):
        super(Node, self).__init__()


class Edge(Attributable):
    def __init__(self, node1: Node, node2: Node):
        super(Edge, self).__init__()
        self._node_from = node1
        self._node_to = node2

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


class Graph:
    def __init__(self, nodes: List[Node], edges: List[Edge]):
        self._nodes = nodes
        self._edges = edges

    def clear(self) -> None:
        self._nodes = []
        self._edges = []

    def add_node(self, v: Node):
        self._nodes.append(v)

    def add_edge(self, e: Edge):
        self._edges.append(e)

    def search(self, query: str, search_nodes: bool = True, search_edges: bool = False) -> "Graph":
        """
            Desc:
                Perform search under the whole graph.

            Args:
                query: str - the text query to search for.
                search_nodes: bool - specifies whether node attributes should satisfy query
                search_edges: bool - specifies whether edge attributes should satisfy query

            Returns:
                A subgraph (Graph) whose elements are
                nodes which satisfy the search with given
                search query.
        """

        if len(self._nodes) == 0:
            raise Exception("Graph is empty")

        if (search_nodes is False) and (search_edges is False):
            return Graph(self.nodes, self.edges)

        qualifying_nodes = set()
        qualifying_edges = set()

        extra_nodes = set()

        if search_nodes:
            qualifying_nodes = self._search_and_collect(query, self.nodes)
            if not search_edges:
                for edge in self._edges:
                    if edge.node_to in qualifying_nodes or edge.node_from in qualifying_nodes:
                        qualifying_edges.add(edge)
                        extra_nodes.add(edge.node_to)
                        extra_nodes.add(edge.node_from)
        if search_edges:
            qualifying_edges = self._search_and_collect(query, self.edges)
            if not search_nodes:
                for edge in qualifying_edges:
                    extra_nodes.add(edge.node_to)
                    extra_nodes.add(edge.node_from)

        return Graph(list(qualifying_nodes.union(extra_nodes)), list(qualifying_edges))

    @staticmethod
    def _search_and_collect(query: str, to_search: List[Attributable]):
        return {element for element in to_search if element.satisfies_query(query)}

    def filter(self, attr_name: str, val: str, operator: Callable[[Any, Any], bool]) -> "Graph":
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

        # TODO: Implementation needed.

        return Graph()

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

