import networkx as nx
import matplotlib.pyplot as plt

from graphviz import Digraph


# Graph display function basic implimentation to check graph logic is sound
def draw_graph_mplib(nodes, connections):
    """
    nodes: list of all node objects in our graph
    connections: list of all connections

    connections can be gen from nodes but for now just pipe in

    # TODO: generate connections in function
    # CODE TO GEN connections
    for i in nodes:
        for j in i.neighbors:
            all_connections.append((i.name, j.name))
    """
    # Init graph object
    G = nx.MultiDiGraph()
    # Add our nodes
    G.add_nodes_from([i.name for i in nodes])
    # Add our edges
    G.add_edges_from(connections)

    # Labeling and coloring graph
    node_colors = ["green"]+["blue"]*(len(nodes)-2) + ["red"]

    labels = {}
    for index, i in enumerate(nodes):
        labels[index] = i.name

    # Create and display the graph
    nx.draw(G, node_color=node_colors, labels=labels, with_labels=True)
    plt.show()


def draw_graphviz(nodes, connections):
    dot = Digraph(comment = "Maze", format="png")
    for i in nodes:
        print(i.name)
        dot.node(str(i.name), "TEst")
    dot.edges(connections)
    dot.render("test.png", view=True)


