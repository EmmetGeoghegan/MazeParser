import display_graph as dg

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
print(len(test_maze))


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

for index, i in enumerate(test_maze):
    layer += 1
    for jindex, j in enumerate(i):
        if j == "o":
            print("o found")
            print(f"o_loc{(index,jindex)}")
            print(layer, len(test_maze), index)
            # check left
            if test_maze[layer][index-1] == "o":
                print("Something to the left")
            # check right
            if test_maze[layer][index-1] == "o":
                print("Something to the right")
            # check up
            if layer != 0:
                print(layer, index)
                if test_maze[layer-1][index-1] == "o":
                    print("Something above")
            # check down
            if layer != len(test_maze)-1:
                if test_maze[layer+1][index-1] == "o":
                    print("Something below")
            o_loc.append([index, jindex])

print("==================")
print("==================")
print(o_loc)

for name, i in enumerate(o_loc):
    Nodes(i, name)

for i in Nodes.all_Nodes:
    print(f"Source: ({i.xpos},{i.ypos}) NAME:{i.name}")
    for j in Nodes.all_Nodes:
        if i != j:
            if (0 <= abs(i.xpos-j.xpos) <= 1):
                if (0 <= abs(i.ypos-j.ypos) <= 1):
                    if abs(i.xpos-j.xpos) != abs(i.ypos-j.ypos):
                        print(f"------Adjacent({j.xpos},{j.ypos})")
                        i.AddNeighbor(j)

print("==================")
print("==================")

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

# for i in Nodes.all_Nodes:
#     print(i.name)

# TODO: Re-factor the class structure to make a linked list
# TODO: Add node removal method
# TODO: Add remapping after node removal method
