import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from graphviz import Digraph
# from anytree import Node, RenderTree
# from anytree.exporter import DotExporter


# Graph display function basic implimentation to check graph logic is sound
def draw_graph_mplib(nodes, connections):
    # Init graph object
    G = nx.MultiDiGraph()
    # Add our nodes
    G.add_nodes_from([i.name for i in nodes])
    print(len(nodes))
    # Add our edges
    G.add_edges_from(connections)

    # Labeling and coloring graph
    node_colors = ["green"]+["lightblue"]*(len(nodes)-2) + ["red"]

    labels = {}
    for index, i in enumerate(nodes):
        labels[i.name] = i.name
    print(labels)

    nx.draw(G, node_color=node_colors, labels=labels)  # , node_color=node_colors, labels=labels, with_labels=True)
    plt.show()


def draw_graphviz(nodes, connections):
    dot = Digraph(comment="Maze", format="png")
    for i in nodes:
        print(i.name)
        dot.node(str(i.name), "TEst")
    dot.edges(connections)
    dot.render("test.png", view=True)


# def draw_networkx(connections):
#     con_from = []
#     con_to = []
#     for i in connections:
#         con_from.append(i[0])
#         con_to.append(i[1])
#     df = pd.DataFrame({"from": con_from, "to": con_to})
#
#     G = nx.from_pandas_edgelist(df, "from", "to")
#     # Fruchterman Reingold
#     nx.draw(G, with_labels=True, node_size=3, node_color="skyblue", pos=nx.nx_agraph.graphviz_layout(G, prog="neato"))
#     plt.title("fruchterman_reingold")
#     plt.show()
#     # pip install pygraphviz
#     # Fruchterman Reingold
#     nx.draw(G, with_labels=True, node_size=1, node_color="skyblue", layout=layout_reingold_tilford)
#     plt.title("fruchterman_reingold")
#     plt.show()
#     # pip install pygraphviz


def render_tree(nodes):
    start = Node("start")
    for i in nodes:
        Node(i.name, parent=i.PrvNode.name)

    print(RenderTree(start))
