import math
import heapq

class vertexMinPQ:
    def __init__(self):
        self._queue = []
        self.entry_finder = dict({i[-1]: i for i in self._queue})
        self.REMOVED = '<removed>'
        self._index = 0

    def push(self, vertex, priority):
        if vertex in self.entry_finder:
            self.delete(vertex)
        item = [priority, self._index, vertex]
        self._index += 1
        self.entry_finder[vertex] = item
        heapq.heappush(self._queue, item)

    def delete(self, vertex):
        item = self.entry_finder.pop(vertex)
        item[-1] = self.REMOVED
        return item[0]

    def pop(self):
        while self._queue:
            #print(self._queue)
            priority, _, vertex = heapq.heappop(self._queue)
            if vertex is not self.REMOVED:
                del self.entry_finder[vertex]
                return vertex
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return not self.entry_finder


class DijkstraSP:
    def __init__(self, G, s):
        """ Dijkstra SP tree
        Attributes:
            G: An edge-weighted directed graph
            s: source vertex
        """
        self._distTo = {}
        self._edgeTo = []  # edgeto[v] = last edge on shortest s->v path
        pq = vertexMinPQ()

        for v in G.vertices():
            self._distTo[v] = math.inf
        self._distTo[s] = 0.0

        pq.push(s, self._distTo[s])

        while not pq.empty():
            #print(pq.empty())
            v = pq.pop()
            #print('v: {}'.format(v))
            if G.inc(v):
                for edge in G.inc(v):
                    t = edge.tail()
                    h = edge.head()

                    if self._distTo[h] > self._distTo[t] + edge.weight():
                        self._distTo[h] = self._distTo[t] + edge.weight()
                        pq.push(h, self._distTo[h])
                        #print('h: {}'.format(h))

    def shortest_path(self):
        return self._distTo