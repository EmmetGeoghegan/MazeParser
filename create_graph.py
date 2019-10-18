import display_graph as dg
import time

test_maze = [
            ["x", "x", "x", "o", "x", "x"],
            ["x", "o", "x", "o", "o", "x"],
            ["x", "o", "x", "o", "x", "x"],
            ["x", "o", "o", "o", "o", "x"],
            ["x", "x", "x", "o", "x", "x"],
            ["x", "o", "o", "o", "o", "x"],
            ["x", "o", "x", "x", "x", "x"],
]

layer = -1
o_loc = []


class Nodes:
    all_Nodes = []

    def __init__(self, position, name):
        Nodes.all_Nodes.append(self)
        self.name = name
        self.xpos = position[0]
        self.ypos = position[1]

        self.neighbors = []
        self.nextnodes = []

        self.PrvNode = Nodes.all_Nodes[0]
        self.Source = 0
        self.Sink = 0

    def AddNeighbor(self, node):
        self.neighbors.append(node)

    def PrvNode(self, node):
        self.PrvNode = node

    def NextNodes(self, node):
        self.nextnodes.append(node)

    def setSource(self):
        self.Source = 1

    def setSink(self):
        self.Sink = 1

    def PrintAllNeighbor(self):
        all_neighbors = ", ".join([str(i.name) for i in self.nextnodes])
        if len(all_neighbors) == 0:
            return("None")
        return all_neighbors

    def nodeinfo(self):
        print("=======================================")
        print(f"Node Name: {self.name}")
        if self.Source > 0:
            print("Type: Source Node")
        elif self.Sink > 0:
            print("Type: Sink Node")
        elif len(self.nextnodes) == 0:
            print("Type: End Node")
        else:
            print("Type: Normal Node")
        print(f"Previous Node: {self.PrvNode.name}")
        print(f"Next Nodes: {self.PrintAllNeighbor()}")
        print("=======================================")


def explore_tree(node):
    for i in node.neighbors:
        if i.name != node.PrvNode.name:
            node.nextnodes.append(i)
            i.PrvNode = node
            explore_tree(i)


def find_whitespace(maze):
    whitespace = []
    for rownum, row in enumerate(test_maze):
        for colnum, entry in enumerate(row):
            if entry == "o":
                whitespace.append([rownum, colnum])
    return whitespace


def make_nodes(whitespace):
    for NodeID, i in enumerate(whitespace):
        Nodes(i, NodeID)

# Find whitespace in the maze and make our nodes
print("-----------------------------------")
print("Finding Whitespace and Making Nodes")
print("-----------------------------------")
print("")

tstart = time.time()
make_nodes(find_whitespace(test_maze))
tend = time.time()

print("----")
print("Done")
print("----")
print(f"Took {round(tend-tstart, 2)} seconds")

def find_adjacent_nodes(AllNodes):
    
for i in Nodes.all_Nodes:
    # print(f"Source: ({i.xpos},{i.ypos}) NAME:{i.name}")
    for j in Nodes.all_Nodes:
        if i != j:
            if (0 <= abs(i.xpos-j.xpos) <= 1):
                if (0 <= abs(i.ypos-j.ypos) <= 1):
                    if abs(i.xpos-j.xpos) != abs(i.ypos-j.ypos):
                        # print(f"------Adjacent({j.xpos},{j.ypos})")
                        i.AddNeighbor(j)

print("")
print("")

all_connections = []
for i in Nodes.all_Nodes:
    for j in i.neighbors:
        # if (j.name, i.name) not in all_connections:
        all_connections.append((i.name, j.name))
print(all_connections)

print("==================")
print("==================")

uselessnodes = []
for i in Nodes.all_Nodes:
    if len(i.neighbors) == 2:
        print(f"Node {i.name} is useless")

print("==================")
print("==================")

# TODO: Add node removal method
# TODO: Add remapping after node removal method

# dg.draw_graph_mplib(Nodes.all_Nodes, all_connections)

Nodes.setSink(Nodes.all_Nodes[-1])
Nodes.setSource(Nodes.all_Nodes[0])

print("-------------------------")
print("Starting Tree Exploration")
print("-------------------------")
print("")
tstart = time.time()

start_node = Nodes.all_Nodes[0]
explore_tree(start_node)

tend = time.time()
print("-------------------")
print("Tree Explored Fully")
print("-------------------")
print(f"Took {round(tend-tstart, 2)} seconds")
print("")
for i in Nodes.all_Nodes:
    Nodes.nodeinfo(i)
