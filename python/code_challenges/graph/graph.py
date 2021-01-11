class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def __len__(self):
        return len(self.adjacency_list)
        # returns number of keys from list

    def add_node(self, value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, starting_vertex, ending_vertex, weight=0):
        if starting_vertex not in self.adjacency_list:
            raise KeyError('no starting vertex')
        if ending_vertex not in self.adjacency_list:
            raise KeyError('no ending vertex')

        edge = Edge(ending_vertex, weight)

        edges = self.adjacency_list[starting_vertex]
        edges.append(edge)

    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbors(self, vertex):
        neighbors = []
        edges = self.adjacency_list.get(vertex, [])
        for neighbor in edges:
            spot = {}
            spot[neighbor] = neighbor.weight
            neighbors.append(spot)
        return neighbors

    def size(self):
        return len(self.adjacency_list)
        


class Vertex:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return ('value is' + self.value)

class Edge:
    def __init__(self, vertex, weight=0)
    self.vertex = vertex
    self.weight = weight
