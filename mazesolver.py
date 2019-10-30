import time
import sys
import interpret_maze as im
import create_graph as cg


def main(maze_name):
    print("---------------")
    print("Generating Maze")
    print("---------------")
    tstart = time.time()
    maze = im.generate_text_maze(maze_name)
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-----------------------------------")
    print("Finding Whitespace and Making Nodes")
    print("-----------------------------------")
    tstart = time.time()
    cg.find_whitespace(maze)
    cg.Graph.all_Nodes[0].source = 1
    cg.Graph.all_Nodes[-1].sink = 1
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-------------------------")
    print("Finding Node Neighbors")
    print("-------------------------")
    tstart = time.time()
    cg.find_node_neighbors(cg.Graph.all_Nodes)
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-----------------")
    print("Sorting Neighbors")
    print("-----------------")
    tstart = time.time()
    start_node = cg.Graph.all_Nodes[0]
    cg.get_next_nodes(start_node, 0, 0)
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("---------------------------")
    print("Removing Unnecessary Nodes")
    print("---------------------------")
    tstart = time.time()
    cg.clean_graph(cg.Graph.all_Nodes)
    cg.Graph.all_Nodes = [i for i in cg.Graph.all_Nodes if i.remove == 0]
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("------------------------")
    print("DFS-ing the path to exit")
    print("------------------------")
    tstart = time.time()
    paths = (cg.dfs_paths(cg.Graph.all_Nodes,
                          cg.Graph.all_Nodes[0],
                          cg.Graph.all_Nodes[-1]))
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("Drawing the maze")
    im.draw_solution(maze_name, paths)


if __name__ == '__main__':
    sys.setrecursionlimit(19000)
    maze_name = input("Plz enter maze name: ")
    maze_name = "10x10.bmp"
    maze_name = "20x20.bmp"
    maze_name = "100x100.bmp"
    maze_name = "200x200.bmp"

    # TODO: Fix Stack overflow for larger mazes
    # maze_name = "300x300.bmp"
    # maze_name = "400x400.bmp"

    print(maze_name)
    main(maze_name)
