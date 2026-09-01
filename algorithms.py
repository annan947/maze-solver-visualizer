import time
import heapq
from collections import deque

from config import ROWS, COLS


# --------------------------------------------------
# FIND VALID NEIGHBORS
# --------------------------------------------------

def get_neighbors(maze, cell):
    row, col = cell

    neighbors = []

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
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
# RECONSTRUCT PATH
# --------------------------------------------------

def reconstruct_path(parent, start, end):
    if start == end:
        return [start]

    if end not in parent:
        return []

    path = []

    current = end

    while current != start:
        path.append(current)

        current = parent[current]

    path.append(start)

    path.reverse()

    return path


# --------------------------------------------------
# CREATE RESULT DICTIONARY
# --------------------------------------------------

def create_result(
    name,
    visited_order,
    path,
    execution_time
):
    return {
        "name": name,
        "visited": visited_order,
        "path": path,
        "explored": len(visited_order),
        "path_length": max(len(path) - 1, 0),
        "time": execution_time
    }


# ==================================================
# BFS
# ==================================================

def bfs(maze, start, end):
    start_time = time.perf_counter()

    queue = deque([start])

    visited = {start}

    visited_order = []

    parent = {}

    while queue:
        current = queue.popleft()

        visited_order.append(current)

        if current == end:
            break

        for neighbor in get_neighbors(
            maze,
            current
        ):
            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    path = reconstruct_path(
        parent,
        start,
        end
    )

    execution_time = (
        time.perf_counter()
        - start_time
    )

    return create_result(
        "BFS",
        visited_order,
        path,
        execution_time
    )


# ==================================================
# DFS
# ==================================================

def dfs(maze, start, end):
    start_time = time.perf_counter()

    stack = [start]

    visited = {start}

    visited_order = []

    parent = {}

    while stack:
        current = stack.pop()

        visited_order.append(current)

        if current == end:
            break

        for neighbor in get_neighbors(
            maze,
            current
        ):
            if neighbor not in visited:
                visited.add(neighbor)

                parent[neighbor] = current

                stack.append(neighbor)

    path = reconstruct_path(
        parent,
        start,
        end
    )

    execution_time = (
        time.perf_counter()
        - start_time
    )

    return create_result(
        "DFS",
        visited_order,
        path,
        execution_time
    )


# ==================================================
# DIJKSTRA
# ==================================================

def dijkstra(maze, start, end):
    start_time = time.perf_counter()

    priority_queue = [
        (0, start)
    ]

    distances = {
        start: 0
    }

    parent = {}

    visited = set()

    visited_order = []

    while priority_queue:
        current_distance, current = (
            heapq.heappop(
                priority_queue
            )
        )

        if current in visited:
            continue

        visited.add(current)

        visited_order.append(current)

        if current == end:
            break

        for neighbor in get_neighbors(
            maze,
            current
        ):
            new_distance = (
                current_distance + 1
            )

            if (
                neighbor not in distances
                or
                new_distance
                < distances[neighbor]
            ):
                distances[neighbor] = (
                    new_distance
                )

                parent[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (
                        new_distance,
                        neighbor
                    )
                )

    path = reconstruct_path(
        parent,
        start,
        end
    )

    execution_time = (
        time.perf_counter()
        - start_time
    )

    return create_result(
        "Dijkstra",
        visited_order,
        path,
        execution_time
    )


# ==================================================
# A*
# ==================================================

def heuristic(cell, end):
    row1, col1 = cell
    row2, col2 = end

    return (
        abs(row1 - row2)
        +
        abs(col1 - col2)
    )


def astar(maze, start, end):
    start_time = time.perf_counter()

    priority_queue = [
        (
            heuristic(start, end),
            0,
            start
        )
    ]

    g_score = {
        start: 0
    }

    parent = {}

    visited = set()

    visited_order = []

    while priority_queue:
        (
            estimated_total,
            current_cost,
            current
        ) = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)

        visited_order.append(current)

        if current == end:
            break

        for neighbor in get_neighbors(
            maze,
            current
        ):
            new_cost = current_cost + 1

            if (
                neighbor not in g_score
                or
                new_cost < g_score[neighbor]
            ):
                g_score[neighbor] = new_cost

                parent[neighbor] = current

                estimated_cost = (
                    new_cost
                    +
                    heuristic(
                        neighbor,
                        end
                    )
                )

                heapq.heappush(
                    priority_queue,
                    (
                        estimated_cost,
                        new_cost,
                        neighbor
                    )
                )

    path = reconstruct_path(
        parent,
        start,
        end
    )

    execution_time = (
        time.perf_counter()
        - start_time
    )

    return create_result(
        "A*",
        visited_order,
        path,
        execution_time
    )