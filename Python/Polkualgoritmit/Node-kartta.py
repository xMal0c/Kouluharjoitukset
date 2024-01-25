# Kirjoita node-pohjainen kartta, jonka pohjilta voimme rakentaa polkualgoritmejä.
# Nodessa tulee olla ainakin seuraavat tiedot:
# 1. Nimi
# 2. Yhteydet: Minne ja kuinka pitkä matka.
# 3. Arvo
# Rakenna node-pohja sivulla olevan kuvan mukaisesti.


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def AddConnection(self, node, distance):
        self.connections[node.name] = distance

    def __repr__(self):
        return f"Node {self.name}"


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


for node in [node_a, node_b, node_c, node_d, node_e, node_f, node_g]:
    print(f"{node}:")
    print(f"   - Yhteydet:")
    for ConnectedNode, distance in node.connections.items():
        print(f"      - {ConnectedNode}: {distance}")
    print()
