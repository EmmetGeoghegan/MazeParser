import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


def draw_networkx(connections):
    print("====")
    print(connections)
    print("-")
    con_from = []
    con_to = []
    for i in connections:
        con_from.append(i[0])
        con_to.append(i[1])
    df = pd.DataFrame({"from": con_from, "to": con_to})

    G = nx.from_pandas_edgelist(df, "from", "to")
    pos = nx.planar_layout(G)

    node_colors = ["green"]+["skyblue"]*(len(G.nodes())-2) + ["red"]

    carac = pd.DataFrame({'ID': G.nodes(), 'myvalue': node_colors})
    carac = carac.set_index('ID')
    carac = carac.reindex(G.nodes())

    nx.draw(G, pos=pos, node_size=100, node_color=carac['myvalue'], with_labels=True)  # , node_color="skyblue")
    plt.title("Graph Representation")
    plt.show()
