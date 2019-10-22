import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


def draw_network(connections):
    # Connection Containers
    con_from = []
    con_to = []

    # Fill connection containers from our connections list
    for i in connections:
        con_from.append(i[0])
        con_to.append(i[1])

    # Create a dataframe to represent our connections
    df = pd.DataFrame({"from": con_from, "to": con_to})

    # Produce the edges from the dataframe
    G = nx.from_pandas_edgelist(df, "from", "to")

    # Color our nodes
    node_colors = ["green"]+["skyblue"]*(len(G.nodes())-2) + ["red"]

    # Apply the colors to the nodes
    carac = pd.DataFrame({'ID': G.nodes(), 'myvalue': node_colors})
    carac = carac.set_index('ID')
    carac = carac.reindex(G.nodes())

    # Type of graph we want, in this case a planar graph representation
    pos = nx.planar_layout(G)
    # Draw the graph
    nx.draw(G, pos=pos, node_size=100, node_color=carac['myvalue'], with_labels=True)  # , node_color="skyblue")
    plt.show()


def main():
    print("This script will display any network given")
    print("Please define your network as a list of edges")
    print("Ensure the source is the lowest number and the sink is the highest number")
    print("eg: [[0,1], [1,7], [6,5], [1,6], [5,7]] (0 would be the source and 7 the sink)")

    connections = eval(input("Enter here:"))
    connections.sort(key=lambda x: x[1])

    try:
        draw_network(connections)
    except Exception as e:
        print(e)
        input()


if __name__ == '__main__':
    main()
