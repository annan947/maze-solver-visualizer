import pygame
import random
from collections import deque

pygame.init()

# --------------------------------------------------
# WINDOW SETTINGS
# --------------------------------------------------

WIDTH = 800
HEIGHT = 600

ROWS = 15
COLS = 21

CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver - Animated BFS")

clock = pygame.time.Clock()


# --------------------------------------------------
# COLORS
# --------------------------------------------------

BACKGROUND = (30, 30, 30)
WALL_COLOR = (220, 220, 220)
GRID_COLOR = (80, 80, 80)

START_COLOR = (0, 200, 0)
END_COLOR = (200, 0, 0)

VISITED_COLOR = (150, 100, 220)
PATH_COLOR = (0, 120, 255)


# --------------------------------------------------
# MAZE VARIABLES
# --------------------------------------------------

maze = []

start = (1, 1)

end = (
    ROWS - 2,
    COLS - 2
)

visited_animation = []
path = []

solving = False


# --------------------------------------------------
# CREATE WALL GRID
# --------------------------------------------------

def create_wall_grid():
    new_maze = []

    for row in range(ROWS):
        new_row = []

        for col in range(COLS):
            new_row.append(1)

        new_maze.append(new_row)

    return new_maze


# --------------------------------------------------
# GENERATE MAZE
# Recursive Backtracking
# --------------------------------------------------

def generate_maze():
    global maze
    global path
    global visited_animation
    global solving

    path = []
    visited_animation = []
    solving = False

    maze = create_wall_grid()

    stack = [start]

    maze[start[0]][start[1]] = 0

    directions = [
        (-2, 0),
        (2, 0),
        (0, -2),
        (0, 2)
    ]

    while stack:
        current_row, current_col = stack[-1]

        possible_moves = []

        for row_change, col_change in directions:
            new_row = current_row + row_change
            new_col = current_col + col_change

            if (
                1 <= new_row < ROWS - 1
                and
                1 <= new_col < COLS - 1
                and
                maze[new_row][new_col] == 1
            ):
                possible_moves.append(
                    (new_row, new_col)
                )

        if possible_moves:
            next_row, next_col = random.choice(
                possible_moves
            )

            wall_row = (
                current_row + next_row
            ) // 2

            wall_col = (
                current_col + next_col
            ) // 2

            maze[wall_row][wall_col] = 0

            maze[next_row][next_col] = 0

            stack.append(
                (next_row, next_col)
            )

        else:
            stack.pop()

    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = 0


# --------------------------------------------------
# VALID NEIGHBORS
# --------------------------------------------------

def get_neighbors(row, col):
    neighbors = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row_change, col_change in directions:
        new_row = row + row_change
        new_col = col + col_change

        if (
            0 <= new_row < ROWS
            and
            0 <= new_col < COLS
            and
            maze[new_row][new_col] == 0
        ):
            neighbors.append(
                (new_row, new_col)
            )

    return neighbors


# --------------------------------------------------
# BFS
# Returns visited order AND shortest path
# --------------------------------------------------

def bfs():
    queue = deque([start])

    visited = {start}

    parent = {}

    visited_order = []

    while queue:
        current = queue.popleft()

        visited_order.append(current)

        if current == end:
            break

        row, col = current

        for neighbor in get_neighbors(
            row,
            col
        ):
            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    if end not in visited:
        return visited_order, []

    shortest_path = []

    current = end

    while current != start:
        shortest_path.append(current)

        current = parent[current]

    shortest_path.append(start)

    shortest_path.reverse()

    return visited_order, shortest_path


# --------------------------------------------------
# DRAW MAZE
# --------------------------------------------------

def draw_maze(
    shown_visited,
    shown_path
):
    for row in range(ROWS):
        for col in range(COLS):

            x = col * CELL_WIDTH
            y = row * CELL_HEIGHT

            rect = pygame.Rect(
                x,
                y,
                CELL_WIDTH,
                CELL_HEIGHT
            )

            cell = (row, col)

            if cell == start:
                pygame.draw.rect(
                    screen,
                    START_COLOR,
                    rect
                )

            elif cell == end:
                pygame.draw.rect(
                    screen,
                    END_COLOR,
                    rect
                )

            elif cell in shown_path:
                pygame.draw.rect(
                    screen,
                    PATH_COLOR,
                    rect
                )

            elif cell in shown_visited:
                pygame.draw.rect(
                    screen,
                    VISITED_COLOR,
                    rect
                )

            elif maze[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    WALL_COLOR,
                    rect
                )

            pygame.draw.rect(
                screen,
                GRID_COLOR,
                rect,
                1
            )


# --------------------------------------------------
# FIRST MAZE
# --------------------------------------------------

generate_maze()


# --------------------------------------------------
# ANIMATION VARIABLES
# --------------------------------------------------

shown_visited = []
shown_path = []

visit_index = 0
path_index = 0

animation_stage = "idle"

animation_delay = 20

last_animation_time = 0


# --------------------------------------------------
# GAME LOOP
# --------------------------------------------------

running = True

while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:

            # ------------------------------------------
            # SPACE = BFS SOLVE
            # ------------------------------------------

            if (
                event.key == pygame.K_SPACE
                and
                animation_stage == "idle"
            ):

                visited_animation, path = bfs()

                shown_visited = []
                shown_path = []

                visit_index = 0
                path_index = 0

                animation_stage = "searching"

                print(
                    "BFS started..."
                )


            # ------------------------------------------
            # R = NEW MAZE
            # ------------------------------------------

            if event.key == pygame.K_r:

                generate_maze()

                shown_visited = []
                shown_path = []

                visit_index = 0
                path_index = 0

                animation_stage = "idle"

                print(
                    "Generated new maze."
                )


            # ------------------------------------------
            # C = CLEAR SOLUTION
            # ------------------------------------------

            if event.key == pygame.K_c:

                shown_visited = []
                shown_path = []

                visit_index = 0
                path_index = 0

                animation_stage = "idle"

                print(
                    "Solution cleared."
                )


    # --------------------------------------------------
    # BFS SEARCH ANIMATION
    # --------------------------------------------------

    if animation_stage == "searching":

        if (
            current_time
            - last_animation_time
            >= animation_delay
        ):

            if visit_index < len(
                visited_animation
            ):

                cell = visited_animation[
                    visit_index
                ]

                if (
                    cell != start
                    and
                    cell != end
                ):
                    shown_visited.append(
                        cell
                    )

                visit_index += 1

                last_animation_time = (
                    current_time
                )

            else:

                if path:
                    animation_stage = (
                        "showing_path"
                    )

                    print(
                        "BFS found the shortest path!"
                    )

                    print(
                        "Path length:",
                        len(path)
                    )

                    print(
                        "Cells explored:",
                        len(
                            visited_animation
                        )
                    )

                else:
                    animation_stage = "idle"

                    print(
                        "No path found."
                    )


    # --------------------------------------------------
    # PATH ANIMATION
    # --------------------------------------------------

    elif animation_stage == "showing_path":

        if (
            current_time
            - last_animation_time
            >= animation_delay
        ):

            if path_index < len(path):

                cell = path[
                    path_index
                ]

                if (
                    cell != start
                    and
                    cell != end
                ):
                    shown_path.append(
                        cell
                    )

                path_index += 1

                last_animation_time = (
                    current_time
                )

            else:

                animation_stage = "idle"

                print(
                    "Animation complete."
                )


    # --------------------------------------------------
    # DRAW
    # --------------------------------------------------

    screen.fill(
        BACKGROUND
    )

    draw_maze(
        shown_visited,
        shown_path
    )

    pygame.display.flip()

    clock.tick(60)


# --------------------------------------------------
# CLOSE
# --------------------------------------------------

pygame.quit()