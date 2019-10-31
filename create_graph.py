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
        self.visited = False

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

    # Pretty print node indepth info
    def nodeinfo(self):
        print("=======================================")
        print(f"Node Name: {self.name}")
        if self.source > 0:
            print("Type: Source Node")
        elif self.sink > 0:
            print("Type: Sink Node")
        elif len(self.neighbors) == 0:
            print("Type: End Node")
        else:
            print("Type: Normal Node")
        print(f"Neighbors: {self.neighbors}")
        print("=======================================")

    # prints all not yet visited vertices
    # reachable from s
    def DFS_TEST(self):
        # Create a stack for DFS
        stack = []
        # Push the current source node.
        stack.append([self, [self]])
        my_path = []
        while (len(stack) != 0):
            # Pop a vertex from stack and start
            node = stack.pop()
            best_path = node[1]
            node = node[0]
            if not node.visited:
                # print(node, end=" ")
                my_path.append(node)
                node.visited = True
            if node.sink == 1:
                return my_path, best_path
            node.neighbors.sort(key=lambda x: x.name)
            for i in node.neighbors:
                if i.visited is False:
                    stack.append([i, best_path+[i]])


################################################################################


# Find the co-ords of the whitespace in the maze O(n)
# Create the node then add it to the appropriate sub-container
def find_whitespace(Maze):
    row_containers = []
    column_containers = []
    for i in range(len(Maze[1])):
        column_containers.append([])
    Node_ID = 0
    for rownum, row in enumerate(Maze):
        row_containers.append([])
        for colnum, entry in enumerate(row):
            if entry == "o":
                this_node = Graph([rownum, colnum], Node_ID)
                row_containers[rownum].append(this_node)
                column_containers[colnum].append(this_node)
                Node_ID += 1
    Graph.row_containers = row_containers
    Graph.column_containers = column_containers


# Figure out if a node is a neighbor to another node O(n^2)
def find_node_neighbors(AllNodes):
    for i in AllNodes:
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
            
        valid_nodes = list(set(possible_nodes_x).intersection(set(possible_nodes_y)))
        for j in valid_nodes:
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
