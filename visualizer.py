import pygame

from config import (
    WIDTH,
    GRID_HEIGHT,
    ROWS,
    COLS,
    CELL_WIDTH,
    CELL_HEIGHT,
    BACKGROUND,
    WALL_COLOR,
    GRID_COLOR,
    START_COLOR,
    END_COLOR,
    VISITED_COLOR,
    PATH_COLOR,
    TEXT_COLOR,
    SECONDARY_TEXT
)


# -----------------------------------------
# DRAW MAZE
# -----------------------------------------

def draw_maze(
    screen,
    maze,
    start,
    end,
    shown_visited,
    shown_path
):

    visited_set = set(shown_visited)
    path_set = set(shown_path)

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

            # Start
            if cell == start:
                pygame.draw.rect(
                    screen,
                    START_COLOR,
                    rect
                )

            # End
            elif cell == end:
                pygame.draw.rect(
                    screen,
                    END_COLOR,
                    rect
                )

            # Final path
            elif cell in path_set:
                pygame.draw.rect(
                    screen,
                    PATH_COLOR,
                    rect
                )

            # Explored cells
            elif cell in visited_set:
                pygame.draw.rect(
                    screen,
                    VISITED_COLOR,
                    rect
                )

            # Walls
            elif maze[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    WALL_COLOR,
                    rect
                )

            # Grid outline
            pygame.draw.rect(
                screen,
                GRID_COLOR,
                rect,
                1
            )


# -----------------------------------------
# DRAW TEXT
# -----------------------------------------

def draw_text(
    screen,
    text,
    font,
    x,
    y,
    color=TEXT_COLOR
):

    surface = font.render(
        text,
        True,
        color
    )

    screen.blit(
        surface,
        (x, y)
    )


# -----------------------------------------
# DRAW HUD
# -----------------------------------------

def draw_hud(
    screen,
    selected_algorithm,
    result,
    comparison_results
):

    pygame.draw.rect(
        screen,
        BACKGROUND,
        (
            0,
            GRID_HEIGHT,
            WIDTH,
            160
        )
    )

    font = pygame.font.Font(
        None,
        28
    )

    small_font = pygame.font.Font(
        None,
        23
    )

    y = GRID_HEIGHT + 10

    draw_text(
        screen,
        f"Selected: {selected_algorithm}",
        font,
        15,
        y
    )

    draw_text(
        screen,
        "1 BFS   2 DFS   3 Dijkstra   4 A*   SPACE Run   R New Maze   C Clear   M Compare",
        small_font,
        15,
        y + 32,
        SECONDARY_TEXT
    )

    # Current algorithm results
    if result is not None:

        info = (
            f"{result['name']} | "
            f"Path: {result['path_length']} | "
            f"Explored: {result['explored']} | "
            f"Time: {result['time'] * 1000:.4f} ms"
        )

        draw_text(
            screen,
            info,
            small_font,
            15,
            y + 65
        )

    # Comparison results
    if comparison_results:

        comparison_text = ""

        for item in comparison_results:

            comparison_text += (
                f"{item['name']}: "
                f"{item['explored']} explored, "
                f"{item['time'] * 1000:.3f} ms    "
            )

        draw_text(
            screen,
            comparison_text,
            small_font,
            15,
            y + 98,
            SECONDARY_TEXT
        )