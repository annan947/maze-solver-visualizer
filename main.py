import pygame

from config import (
    WIDTH,
    HEIGHT,
    BACKGROUND,
    START,
    END,
    ANIMATION_DELAY
)

from maze import generate_maze

from algorithms import (
    bfs,
    dfs,
    dijkstra,
    astar
)

from visualizer import (
    draw_maze,
    draw_hud
)


# -----------------------------------------
# INITIALIZE PYGAME
# -----------------------------------------

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Pathfinding Algorithm Visualizer"
)

clock = pygame.time.Clock()


# -----------------------------------------
# ALGORITHMS
# -----------------------------------------

algorithms = {
    "BFS": bfs,
    "DFS": dfs,
    "Dijkstra": dijkstra,
    "A*": astar
}


# -----------------------------------------
# INITIAL GAME STATE
# -----------------------------------------

maze = generate_maze()

selected_algorithm = "BFS"

current_result = None

comparison_results = []


# -----------------------------------------
# ANIMATION STATE
# -----------------------------------------

shown_visited = []

shown_path = []

visit_index = 0

path_index = 0

animation_stage = "idle"

last_animation_time = 0


# -----------------------------------------
# CLEAR VISUALIZATION
# -----------------------------------------

def clear_visualization():

    global shown_visited
    global shown_path

    global visit_index
    global path_index

    global animation_stage

    global current_result

    shown_visited = []
    shown_path = []

    visit_index = 0
    path_index = 0

    animation_stage = "idle"

    current_result = None


# -----------------------------------------
# RUN SELECTED ALGORITHM
# -----------------------------------------

def start_algorithm():

    global current_result

    global shown_visited
    global shown_path

    global visit_index
    global path_index

    global animation_stage

    algorithm_function = (
        algorithms[selected_algorithm]
    )

    current_result = algorithm_function(
        maze,
        START,
        END
    )

    shown_visited = []
    shown_path = []

    visit_index = 0
    path_index = 0

    animation_stage = "searching"

    print(
        f"\nRunning "
        f"{selected_algorithm}..."
    )


# -----------------------------------------
# COMPARE ALL ALGORITHMS
# -----------------------------------------

def compare_algorithms():

    results = []

    print(
        "\n"
        "----------------------------------------"
    )

    print(
        "ALGORITHM COMPARISON"
    )

    print(
        "----------------------------------------"
    )

    for name, function in algorithms.items():

        result = function(
            maze,
            START,
            END
        )

        results.append(result)

        print(
            f"{name:10} | "
            f"Path: "
            f"{result['path_length']:3} | "
            f"Explored: "
            f"{result['explored']:3} | "
            f"Time: "
            f"{result['time'] * 1000:.4f} ms"
        )

    print(
        "----------------------------------------"
    )

    return results


# -----------------------------------------
# GAME LOOP
# -----------------------------------------

running = True

while running:

    current_time = (
        pygame.time.get_ticks()
    )

    # -------------------------------------
    # EVENTS
    # -------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.KEYDOWN:

            # -----------------------------
            # SELECT BFS
            # -----------------------------

            if event.key == pygame.K_1:

                selected_algorithm = "BFS"

                clear_visualization()


            # -----------------------------
            # SELECT DFS
            # -----------------------------

            elif event.key == pygame.K_2:

                selected_algorithm = "DFS"

                clear_visualization()


            # -----------------------------
            # SELECT DIJKSTRA
            # -----------------------------

            elif event.key == pygame.K_3:

                selected_algorithm = (
                    "Dijkstra"
                )

                clear_visualization()


            # -----------------------------
            # SELECT A*
            # -----------------------------

            elif event.key == pygame.K_4:

                selected_algorithm = "A*"

                clear_visualization()


            # -----------------------------
            # RUN ALGORITHM
            # -----------------------------

            elif (
                event.key
                == pygame.K_SPACE
            ):

                start_algorithm()


            # -----------------------------
            # NEW MAZE
            # -----------------------------

            elif event.key == pygame.K_r:

                maze = generate_maze()

                clear_visualization()

                comparison_results = []

                print(
                    "\nGenerated new maze."
                )


            # -----------------------------
            # CLEAR
            # -----------------------------

            elif event.key == pygame.K_c:

                clear_visualization()

                comparison_results = []


            # -----------------------------
            # COMPARE
            # -----------------------------

            elif event.key == pygame.K_m:

                comparison_results = (
                    compare_algorithms()
                )


    # =====================================
    # SEARCH ANIMATION
    # =====================================

    if animation_stage == "searching":

        if (
            current_time
            - last_animation_time
            >= ANIMATION_DELAY
        ):

            visited = (
                current_result["visited"]
            )

            if visit_index < len(
                visited
            ):

                cell = visited[
                    visit_index
                ]

                if (
                    cell != START
                    and
                    cell != END
                ):

                    shown_visited.append(
                        cell
                    )

                visit_index += 1

                last_animation_time = (
                    current_time
                )

            else:

                animation_stage = (
                    "showing_path"
                )


    # =====================================
    # PATH ANIMATION
    # =====================================

    elif animation_stage == "showing_path":

        if (
            current_time
            - last_animation_time
            >= ANIMATION_DELAY
        ):

            path = (
                current_result["path"]
            )

            if path_index < len(path):

                cell = path[
                    path_index
                ]

                if (
                    cell != START
                    and
                    cell != END
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
                    f"{current_result['name']} "
                    f"finished."
                )

                print(
                    "Path length:",
                    current_result[
                        "path_length"
                    ]
                )

                print(
                    "Cells explored:",
                    current_result[
                        "explored"
                    ]
                )

                print(
                    "Execution time:",
                    (
                        current_result[
                            "time"
                        ]
                        * 1000
                    ),
                    "ms"
                )


    # -------------------------------------
    # DRAW
    # -------------------------------------

    screen.fill(
        BACKGROUND
    )

    draw_maze(
        screen,
        maze,
        START,
        END,
        shown_visited,
        shown_path
    )

    draw_hud(
        screen,
        selected_algorithm,
        current_result,
        comparison_results
    )

    pygame.display.flip()

    clock.tick(60)


pygame.quit()