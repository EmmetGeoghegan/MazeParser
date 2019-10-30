import cv2
from PIL import Image
import os
import shutil


def generate_text_maze(image, wall_symbol="x", path_symbol="o"):
    # Read in the image into memory
    image = cv2.imread(f".//mazes//{image}")
    # Maze container
    maze = []
    # Loop through maze and get pixel values
    for row in range(image.shape[0]):
        # Maze row container
        maze_row = []
        # Move across maze
        for column in range(image.shape[1]):
            # Grab Pixel values and if black its a wall else path
            pixel = image[row, column]
            if pixel[1] == 0:
                maze_row.append(wall_symbol)
            else:
                maze_row.append(path_symbol)
        # Append each row to our maze object
        maze.append(maze_row)
    return maze


def draw_solution(imagename, NodePaths):
    index = 1
    outfile_list = []
    for i in NodePaths:
        while index <= len(i):
            draw_path = []
            for j in range(0, index, 1):
                draw_path.append(i[j])
            index += 1
            image = cv2.imread(f".//mazes//{imagename}")
            for k in draw_path:
                for l in k.draw_path:
                    image[l[0], l[1]] = [0, 0, 255]
            outfile_name = f"./gif/{imagename.split('.')[0]}-{index}.png"
            outfile_list.append(outfile_name)
            cv2.imwrite(outfile_name, image)

        images = []
        for n in outfile_list:
            frame = Image.open(n)
            images.append(frame)

        # Save the frames as an animated GIF
        images[0].save(f"./gif_soln/{imagename.split('.')[0]}.gif",
                       save_all=True,
                       append_images=images[1:],
                       duration=100,
                       loop=0)
        directory = f"{os.getcwd()}\\gif"

        clean_directory(directory)


def clean_directory(directory):
    shutil.rmtree(directory)
    os.mkdir(directory)


def main():
    filename = input("Please enter filename (with extension): ")
    try:
        maze = generate_text_maze(filename)
        print("=====================")
        print("      TEXT MAZE      ")
        print("=====================")
        for i in maze:
            print(str("".join(i)))

    except Exception:
        print("Invalid file name")
        main()


if __name__ == "__main__":
    main()
