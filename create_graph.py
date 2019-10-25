# import display_graph as dg
import interpret_maze as im
import time
import sys

sys.setrecursionlimit(15000)


# test_maze = im.generate_text_maze("21x21.bmp")


# Class to contain our Graph Structure
class Graph:
    # Container for all nodes of the graph
    all_Nodes = []

    def __init__(self, position, name):
        # Setup node
        Graph.all_Nodes.append(self)
        self.name = name
        self.xpos = position[0]
        self.ypos = position[1]

        # Info needed to draw the node
        self.draw_path = [[self.xpos, self.ypos]]
        # Distance traveled to reach the node
        self.distance = 1

        # Initialise with no next features
        self.neighbors = []
        self.nextNodes = []

        # Give the source as the default previous node
        self.prvNode = Graph.all_Nodes[0]

        # Flags for types of node
        self.source = 0
        self.sink = 0
        # Flag that a node is useless, ie its got 2 connections
        self.remove = 0

    def __repr__(self):
        return str(self.name)

    def AddNeighbor(self, node):
        self.neighbors.append(node)

    def SetPrvNode(self, node):
        self.prvNode = node

    def SetNextNodes(self, node):
        self.nextNodes.append(node)

    def SetSource(self):
        self.source = 1

    def MarkForRemoval(self):
        self.remove = 1

    def SetSink(self):
        self.sink = 1

    # Pretty print node indepth info
    def nodeinfo(self):
        print("=======================================")
        print(f"Node Name: {self.name}")
        if self.source > 0:
            print("Type: Source Node")
        elif self.sink > 0:
            print("Type: Sink Node")
        elif len(self.nextNodes) == 0:
            print("Type: End Node")
        else:
            print("Type: Normal Node")
        print(f"Previous Node: {self.prvNode}")
        print(f"Next Nodes: {self.PrintNextNodes()}")
        print("=======================================")

    # Printer helper function
    def PrintNextNodes(self):
        all_neighbors = ", ".join([str(i.name) for i in self.nextNodes])
        if len(all_neighbors) == 0:
            return("None")
        return all_neighbors


################################################################################


# Find the co-ords of the whitespace in the maze O(n)
def find_whitespace(Maze):
    whitespace_coords = []
    for rownum, row in enumerate(Maze):
        for colnum, entry in enumerate(row):
            if entry == "o":
                whitespace_coords.append([rownum, colnum])
    return whitespace_coords


# Seperate the neighbors of a node into previous and next nodes O(n)
def get_next_nodes(Node):
    for i in Node.neighbors:
        """
        This is why we have to __init__ with prvNode as the source.
        It lets us have a link to start on, ie source to the first node
        """
        if i.name != Node.prvNode.name:
            Node.nextNodes.append(i)
            i.prvNode = Node
            # Explore the nodes til done.
            get_next_nodes(i)


# Take [[x,y]*n...] and create nodes O(n)
def make_nodes(Whitespace):
    for NodeID, i in enumerate(Whitespace):
        # Nodes are named based on the order they are read in
        # ie top to bottom, left to right
        Graph(i, NodeID)


# Figure out if a node is a neighbor to another node O(n^2)
def find_node_neighbors(AllNodes):
    # Check every node against every other node
    # TODO: Investigate a way to reduce time complexity
    for i in AllNodes:
        for j in AllNodes:
            # If not checking the same node
            if i != j:
                """
                A B C  If this is our test chunk of maze, we want to find the
                D X E  neighbors of X. They should be [B, D, E, G]
                F G H  Diagonal moves are not possible in our mazes

                We calculate this based on coordinate difference.
                However all A->H are within "1" x and y
                """
                if (0 <= abs(i.xpos-j.xpos) <= 1):
                    if (0 <= abs(i.ypos-j.ypos) <= 1):
                        """
                        A B C  This tests if the xpos and ypos differences are
                        D X E  either 1 or 0. The only nodes to pass this test
                        F G H  Are A->H
                        """
                        if abs(i.xpos-j.xpos) != abs(i.ypos-j.ypos):
                            """
                            . B .  To finally get the neighbors of X we XOR
                            D X E  two different checks. That the difference
                            . G .  in xposition is not equal to the difference
                                   in yposition. [A, C, F, H] all have a
                                   non-zero xpos AND ypos difference. XORing
                                   the checks produce our neighbors [B, D, E, G]
                            """
                            i.AddNeighbor(j)


# Get all forward paths in the network O(n)
def get_paths(Node):
    all_paths = []
    for i in Node.nextNodes:
        all_paths.append([(Node.name), (i.name)])

    return all_paths


# Prune unnecessary nodes
def clean_graph(allNodes):
    # input("START CLEAN")
    for i in allNodes:
        # Useless check
        if len(i.neighbors) == 2:
            # print(f"Node {i.name} is useless")
            # print(i.prvNode, i.nextNodes)
            # print(i.prvNode.nextNodes)
            # print("Before", i.prvNode.nextNodes)

            i.prvNode.nextNodes.remove(i)
            i.prvNode.nextNodes.append(i.nextNodes[0])

            # print("After", i.prvNode.nextNodes)

            i.nextNodes[0].prvNode = i.prvNode

            # Conserve length
            i.nextNodes[0].distance += i.distance

            # Conserve coords of node
            i.nextNodes[0].draw_path += i.draw_path
            # Clear out the node properties
            i.prvNode = None
            i.nextNodes = []
            Graph.MarkForRemoval(i)

            # print(f"Node {i.name} Removed")
    # input("CLEAN OVER")


def main():
    print("---------------")
    print("Generating Maze")
    print("---------------")
    tstart = time.time()
    maze = im.generate_text_maze("20x20.bmp")
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-----------------------------------")
    print("Finding Whitespace and Making Nodes")
    print("-----------------------------------")
    tstart = time.time()
    make_nodes(find_whitespace(maze))
    Graph.SetSource(Graph.all_Nodes[0])
    Graph.SetSink(Graph.all_Nodes[-1])
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-------------------------")
    print("Finding Node Neighbors")
    print("-------------------------")
    tstart = time.time()
    find_node_neighbors(Graph.all_Nodes)
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-----------------")
    print("Sorting Neighbors")
    print("-----------------")
    tstart = time.time()
    start_node = Graph.all_Nodes[0]
    get_next_nodes(start_node)
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("---------------------------")
    print("Removing Unnecessary Nodes")
    print("---------------------------")
    tstart = time.time()
    clean_graph(Graph.all_Nodes)
    Graph.all_Nodes = [i for i in Graph.all_Nodes if i.remove == 0]
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    # print(Graph.all_Nodes)
    # print("--=-=-=-=-=-=-")
    # print(Graph.all_Nodes)
    # Get all node info
    all_paths = []
    for i in Graph.all_Nodes:
        all_paths += get_paths(i)

    all_paths.sort(key=lambda x: x[1])

    # dg.draw_network(all_paths)


#####################
#   Dev Functions   #
#####################

def dfs_paths(All_Nodes, start, end, path=[]):
    # print(path)
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in start.nextNodes:
        if node not in path:
            newpaths = dfs_paths(All_Nodes, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


main()

tstart = time.time()
paths = (dfs_paths(Graph.all_Nodes, Graph.all_Nodes[0], Graph.all_Nodes[-1]))
tend = time.time()

print(f"Done, Took {round(tend-tstart, 2)} seconds")
print("")

# print(paths)

im.draw_solution("200x200.bmp", paths)
