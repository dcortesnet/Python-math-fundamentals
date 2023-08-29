class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

edge_ab = Edge(node_a, node_b)
edge_bc = Edge(node_b, node_c)
edge_ca = Edge(node_c, node_a)

node_a.connections.append(edge_ab)
node_b.connections.append(edge_bc)
node_c.connections.append(edge_ca)