# Kirjoita Dijkstran algoritmi funktio, joka toimii millä tahansa datasetillä. 
# Argumentteina Lähtöindex, Maali-index, Datasetti. Funktio palauttaa listan nopeimmasta reitistä.


class Connection:
    def __init__(self, W, D):
        self.where = W
        self.dist = D

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.value = 10000000000    # Ääretön
        self.shortest = None

    def CreateConnection(self, Name, Dist):
        self.connections.append(Connection(Name, Dist))

    def AddConnection(self, node, distance):
        self.connections.append(Connection(node, distance))

    def __repr__(self):
        return f"Node {self.name}"

def Dijkstra(StartNode, EndNode, nodes):
    StartIndex = StartNode.name
    EndIndex = EndNode.name
    
    # Valitaan tutkittava solu ja sen arvoksi 0
    distances = {node: float('inf') for node in nodes}
    predecessors = {node: None for node in nodes}
    distances[StartIndex] = 0
    
    # Alustetaan jono
    checkqueue = [(0, StartIndex)]
    
    while checkqueue:
        # Valitaan lyhyin solu tutkittavaksi
        current_distance, current_node = min(checkqueue, key=lambda x: x[0])
        checkqueue.remove((current_distance, current_node))
        
        # Päivitetään solujen etäisyydet ja seuraava jono
        for connection in nodes[current_node].connections:
            neighbor, distance = connection.where, connection.dist
            new_distance = distances[current_node] + distance
            if new_distance < distances[neighbor.name]:
                distances[neighbor.name] = new_distance
                predecessors[neighbor.name] = current_node
                checkqueue.append((new_distance, neighbor.name))
    
    # Palautetaan nopein mahdollinen reitti
    path = []
    current_node = EndIndex
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]

    return path


# Nodet
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")

node_a.AddConnection(node_c, 3)
node_a.AddConnection(node_f, 2)

node_b.AddConnection(node_d, 1)
node_b.AddConnection(node_e, 2)
node_b.AddConnection(node_f, 6)
node_b.AddConnection(node_g, 2)

node_c.AddConnection(node_a, 3)
node_c.AddConnection(node_f, 2)
node_c.AddConnection(node_e, 1)
node_c.AddConnection(node_d, 4)

node_d.AddConnection(node_c, 4)
node_d.AddConnection(node_b, 1)

node_e.AddConnection(node_c, 1)
node_e.AddConnection(node_f, 3)
node_e.AddConnection(node_b, 2)

node_f.AddConnection(node_a, 2)
node_f.AddConnection(node_c, 2)
node_f.AddConnection(node_e, 3)
node_f.AddConnection(node_b, 6)
node_f.AddConnection(node_g, 5)

node_g.AddConnection(node_f, 5)
node_g.AddConnection(node_b, 2)


StartNode = node_a
EndNode = node_b
path = Dijkstra(StartNode, EndNode, {node.name: node for node in [node_a, node_b, node_c, node_d, node_e, node_f, node_g]})

print(f"Lyhyin reitti paikasta {StartNode} paikkaan {EndNode} on: {path}")
