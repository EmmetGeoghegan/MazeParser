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

    print("--------")
    print("DFS Time")
    print("--------")
    tstart = time.time()
    visited, best_path = cg.Graph.DFS_TEST(cg.Graph.all_Nodes[0])
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-----------------------")
    print("Drawing Squares Visited")
    print("-----------------------")
    tstart = time.time()
    im.draw_visited(maze_name, [visited])
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("-----------------")
    print("Drawing Best Path")
    print("-----------------")
    tstart = time.time()
    im.draw_path(maze_name, [best_path])
    tend = time.time()
    print(f"Done, Took {round(tend-tstart, 2)} seconds")
    print("")

    print("------------")
    print("Creating Gif")
    print("------------")
    print(f"There are {len(visited)} Frames to draw")
    choice = input("Continue Y/N: ")
    if choice == "Y":
        tstart = time.time()
        im.draw_gif_solution(maze_name, [best_path])
        tend = time.time()
        print(f"Done, Took {round(tend-tstart, 2)} seconds")
        print(f"""Average frame time:
                {round((tend-tstart)/len(best_path), 2)} seconds""")
    print("")


if __name__ == '__main__':
    sys.setrecursionlimit(19000)
    maze_name = input("Plz enter maze name: ")
    maze_name = "10x10.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "20x20.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "100x100.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "200x200.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "300x300.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "400x400.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "600x600.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "800x800.bmp"
    print(maze_name)
    main(maze_name)
    maze_name = "1000x1000.bmp"
    print(maze_name)
    main(maze_name)
