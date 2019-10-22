import cv2


def generate_text_maze(image):
    # Read in the image into memory
    image = cv2.imread(image)
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
                maze_row.append("x")
            else:
                maze_row.append("o")
        # Append each row to our maze object
        maze.append(maze_row)
    return maze

