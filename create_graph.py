import display_graph as dg
import interpret_maze as im
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
test_maze = im.generate_text_maze("21x21.bmp")

class Graph:
    all_Nodes = []

    def __init__(self, position, name):
        Graph.all_Nodes.append(self)
        self.name = name
        self.xpos = position[0]
        self.ypos = position[1]

        self.neighbors = []
        self.nextnodes = []

        self.PrvNode = Graph.all_Nodes[0]
        self.Source = 0
        self.Sink = 0

    def __repr__(self):
        return str(self.name)

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
        Graph(i, NodeID)


def find_adjacent_nodes(AllNodes):
    for i in AllNodes:
        for j in AllNodes:
            if i != j:
                if (0 <= abs(i.xpos-j.xpos) <= 1):
                    if (0 <= abs(i.ypos-j.ypos) <= 1):
                        if abs(i.xpos-j.xpos) != abs(i.ypos-j.ypos):
                            i.AddNeighbor(j)


def get_paths(Node):
    all_paths = []
    for i in Node.nextnodes:
        all_paths.append((str(Node.name), str(i.name)))
    return all_paths


def main():
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

    find_adjacent_nodes(Graph.all_Nodes)

    print("")
    print("")

    all_connections = []
    for i in Graph.all_Nodes:
        for j in i.neighbors:
            # if (j.name, i.name) not in all_connections:
            all_connections.append((i.name, j.name))
    print(all_connections)

    print("==================")
    print("==================")

    for i in Graph.all_Nodes:
        if len(i.neighbors) == 2:
            print(f"Node {i.name} is useless")

    print("==================")
    print("==================")

    Graph.setSink(Graph.all_Nodes[-1])
    Graph.setSource(Graph.all_Nodes[0])

    print("-------------------------")
    print("Starting Tree Exploration")
    print("-------------------------")
    print("")
    tstart = time.time()

    start_node = Graph.all_Nodes[0]
    explore_tree(start_node)

    tend = time.time()
    print("-------------------")
    print("Tree Explored Fully")
    print("-------------------")
    print(f"Took {round(tend-tstart, 2)} seconds")
    print("")

    # Get all node info
    all_paths = []
    for i in Graph.all_Nodes:
        Graph.nodeinfo(i)
        print("")
        all_paths += get_paths(i)

    print(all_paths)

    dg.draw_graph_mplib(Graph.all_Nodes, all_connections)
    dg.draw_graph_mplib(Graph.all_Nodes, all_paths)
    dg.draw_graphviz(Graph.all_Nodes, all_paths)


def dfs_paths(All_Nodes, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in start.nextnodes:
        if node not in path:
            newpaths = dfs_paths(All_Nodes, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


main()

paths = (dfs_paths(Graph.all_Nodes, Graph.all_Nodes[0], Graph.all_Nodes[-1]))

print(paths)
