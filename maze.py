import random

def generate_maze(width, height):
    # Initialize the maze with walls
    maze = [['i'] * (2 * width + 1) for _ in range(2 * height + 1)]

    # Create a list to store visited cells
    visited = [[False] * width for _ in range(height)]

    # Define directions (up, right, down, left)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and not visited[y][x]

    def carve_path(x, y):
        visited[y][x] = True
        maze[2 * y + 1][2 * x + 1] = ' '

        # Randomly shuffle the directions
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy

            if is_valid(nx, ny):
                maze[ny * 2 + 1][nx * 2 + 1] = ' '
                maze[y * 2 + 1 + dy][x * 2 + 1 + dx] = ' '

                carve_path(nx, ny)

    # Start carving from a random cell
    start_x, start_y = random.randrange(width), random.randrange(height)
    carve_path(start_x, start_y)

    # Set entrance and exit
    maze[0][1] = ' '
    maze[2 * height][2 * width - 1] = ' '

    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    width, height = 10, 5  # Adjust the dimensions as needed
    maze = generate_maze(width, height)
    print_maze(maze)
