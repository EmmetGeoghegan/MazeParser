import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd



    # Labeling and coloring graph
    node_colors = ["green"]+["lightblue"]*(len(nodes)-2) + ["red"]

    labels = {}
    for index, i in enumerate(nodes):
        labels[i.name] = i.name
    print(labels)

    nx.draw(G, node_color=node_colors, labels=labels)  # , node_color=node_colors, labels=labels, with_labels=True)
    plt.show()


    node_colors = ["green"]+["skyblue"]*(len(G.nodes())-2) + ["red"]

    carac = pd.DataFrame({'ID': G.nodes(), 'myvalue': node_colors})
    carac = carac.set_index('ID')
    carac = carac.reindex(G.nodes())

    nx.draw(G, pos=pos, node_size=100, node_color=carac['myvalue'], with_labels=True)  # , node_color="skyblue")
    plt.title("Graph Representation")
    plt.show()
