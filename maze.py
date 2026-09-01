import random

from config import ROWS, COLS, START, END


def create_wall_grid():
    maze = []

    for row in range(ROWS):
        new_row = []

        for col in range(COLS):
            new_row.append(1)

        maze.append(new_row)

    return maze


def generate_maze():
    maze = create_wall_grid()

    stack = [START]

    maze[START[0]][START[1]] = 0

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

    maze[START[0]][START[1]] = 0
    maze[END[0]][END[1]] = 0

    return maze