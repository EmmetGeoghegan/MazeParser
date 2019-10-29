# Class to contain our Graph Structure
class Graph:
    # Container for all nodes of the graph
    all_Nodes = []
    row_containers = []
    column_containers = []

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
# Create the node then add it to the appropriate sub-container
def find_whitespace(Maze):
    row_containers = []
    column_containers = []
    for i in range(len(Maze[1])):
        column_containers.append([])
    Node_ID = 0
    while True:
        for rownum, row in enumerate(Maze):
            row_containers.append([])
            for colnum, entry in enumerate(row):
                if entry == "o":
                    this_node = Graph([rownum, colnum], Node_ID)
                    row_containers[rownum].append(this_node)
                    column_containers[colnum].append(this_node)
                    Node_ID += 1
        break
    Graph.row_containers = row_containers
    Graph.column_containers = column_containers


# Seperate the neighbors of a node into previous and next nodes O(n)
def get_next_nodes(Node, depth):
    depth += 1

    for i in Node.neighbors:
        """
        This is why we have to __init__ with prvNode as the source.
        It lets us have a link to start on, ie source to the first node
        """
        if i.name != Node.prvNode.name:
            Node.nextNodes.append(i)
            i.prvNode = Node
            # print("Done node;", i, "Depth", depth)
            # Explore the nodes til done.
            get_next_nodes(i, depth)


# Figure out if a node is a neighbor to another node O(n^2)
def find_node_neighbors(AllNodes):
    # Check every node against every other node
    # TODO: Investigate a way to reduce time complexity
    print(len(AllNodes))
    for i in AllNodes:
        # print(f"Coords:{(i.xpos, i.ypos)} NodeID:{i}")
        # print("in row: ", Graph.row_containers[i.xpos])
        # print("incol: ", Graph.column_containers[i.ypos])
        possible_nodes_x = []
        possible_nodes_y = []
        possible_nodes_x += Graph.row_containers[i.xpos - 1]
        possible_nodes_x += Graph.row_containers[i.xpos]
        try:
            possible_nodes_x += Graph.row_containers[i.xpos + 1]
        except IndexError:
            pass
        possible_nodes_y += Graph.column_containers[i.ypos - 1]
        possible_nodes_y += Graph.column_containers[i.ypos]
        try:
            possible_nodes_y += Graph.column_containers[i.ypos + 1]
        except IndexError:
            pass

        for j in list(set(possible_nodes_x).intersection(set(possible_nodes_y))):
            # If not checking the same node
            if i != j:
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
        # print(f"Node: {i}, Neighbors: {i.neighbors}")


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
