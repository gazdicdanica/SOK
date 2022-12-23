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

        # TODO: Needs implementation
        # TODO: Manual conversion after get_attr (int, float, bool, str)
        # TODO: return operator(my value, val converted)
        return False

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

        # TODO: Needs implementation
        return False


class Graph:
    def __init__(self, nodes: List[Node], edges: List[Edge]):
        self._nodes = nodes
        self._edges = edges

    def clear(self) -> None:
        self._nodes = []
        self._edges = []

    def search(self, query: str) -> List[Tuple[Node, List[str]]]:
        """
            Desc:
                Perform search under the whole graph.

            Args:
                query: str - the text query to search for.

            Returns:
                A list of tuples (Node, List[str]) whose first element is
                a node which satisfies the search, and the second element
                is a list of attributes of that node whose values match
                the search query.

                It's guaranteed that for some tuple (node, li), li is NOT empty. 
        """

        # TODO: Implementation needed.

        return []

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