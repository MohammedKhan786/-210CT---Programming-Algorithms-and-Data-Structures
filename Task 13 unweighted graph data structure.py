class Vertex:
    def __init__(self, l):
        self.name = l
        self.neighbors = list()


class Graph:
    vertices = {}

    def add_node(self, node):
        self.vertices[node.name] = node
			
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].neighbors.append(v)
            self.vertices[v].neighbors.append(u)
			
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

g = Graph()
g.add_node(Vertex('A'))
g.add_node(Vertex('B'))
g.add_node(Vertex('C'))
g.add_node(Vertex('D'))
g.add_node(Vertex('E'))
g.add_node(Vertex('F'))
g.add_node(Vertex('G'))
g.add_node(Vertex('H'))
g.add_node(Vertex('I'))

g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('B', 'C')
g.add_edge('H', 'B')
g.add_edge('H', 'C')
g.add_edge('D', 'C')
g.add_edge('D', 'F')
g.add_edge('D', 'E')
g.add_edge('E', 'F')
g.add_edge('H', 'G')
g.add_edge('H', 'I')
g.add_edge('G', 'I')
g.add_edge('G', 'C')

g.print_graph()


