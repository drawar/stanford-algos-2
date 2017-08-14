from collections import defaultdict

class DirectedEdge(object):
    """ A directed weighted edge
    Attributes:
        v: tail node
        w: head node
        weight: edge weight
    """

    def __init__(self, v, w, weight=1.0):
        """ Return a DirectedEdge object whose tail and head nodes and its weight
         are v, w, and *weight* respectively"""
        self.v = v
        self.w = w
        self._weight = weight

    def weight(self):
        """ Return weight
        """
        return self._weight

    def tail(self):
        """ Return tail node
        """
        return self.v

    def head(self):
        """ Return head node
        """
        return self.w

    def __str__(self):
        return str(self.v) + '->' + str(self.w) + ' ' + str(self.weight)


class EdgeWeightedDigraph(object):
    """ An edge-weighted directed graph
    Attributes:
        V: number of vertices
        E: number of edges
        adj: adjacency lists
    """

    def __init__(self, edges):
        self._inc = defaultdict(set)
        self._adj = defaultdict(set)
        self._edges = edges
        self._vertices = set()
        for edge in edges:
            self.add_edge(edge)
            self._vertices.add(edge.tail())
            self._vertices.add(edge.head())

    def add_edge(self, edge):
        self._inc[edge.tail()].add(edge)
        self._adj[edge.tail()].add(edge.head())

    def inc(self, v):
        return self._inc[v]

    def adj(self, v):
        return self._adj[v]

    def V(self):
        return len(self._vertices)

    def E(self):
        return len(self._edges)

    def edges(self):
        return self._edges

    def vertices(self):
        return self._vertices
