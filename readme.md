# Maze Solver & Pathfinding Visualizer

A Python and Pygame application that generates random mazes and visualizes multiple pathfinding algorithms as they search for a solution.

The project allows users to compare **Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, **Dijkstra's Algorithm**, and **A\* Search** on the same randomly generated maze.

Each algorithm is animated so its search process can be observed in real time. The program also measures path length, number of cells explored, and execution time to demonstrate the differences between pathfinding strategies.

---

## Features

- Random maze generation
- Recursive backtracking maze-generation algorithm
- Animated pathfinding visualization
- Four pathfinding algorithms:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Dijkstra's Algorithm
  - A* Search
- Shortest-path reconstruction
- Algorithm performance statistics
- Number of cells explored
- Final path length
- Algorithm execution time
- Compare all four algorithms on the same maze
- Generate new mazes without restarting the program
- Clear and rerun algorithms
- Modular Python project structure

---

## Demo

The program generates a new maze containing a starting point and destination.

After selecting an algorithm, the visualization shows the cells explored during the search followed by the final path.

### Visualization Colors

| Color | Meaning |
|---|---|
| 🟢 Green | Starting position |
| 🔴 Red | Destination |
| 🟣 Purple | Explored cells |
| 🔵 Blue | Final path |
| ⬜ White / Gray | Maze walls |

---

## Controls

| Key | Action |
|---|---|
| `1` | Select Breadth-First Search |
| `2` | Select Depth-First Search |
| `3` | Select Dijkstra's Algorithm |
| `4` | Select A* Search |
| `SPACE` | Run and animate the selected algorithm |
| `M` | Compare all algorithms |
| `R` | Generate a new random maze |
| `C` | Clear the current visualization |

---

## Pathfinding Algorithms

### Breadth-First Search (BFS)

BFS explores the maze level by level using a **queue**.

It explores all nearby cells before moving farther away from the starting position.

Because every movement in the maze has the same cost, BFS guarantees a shortest path to the destination.

**Data structure:** Queue (`deque`)

---

### Depth-First Search (DFS)

DFS follows one path as far as possible before backtracking and exploring another route.

It uses a **stack** rather than a queue.

DFS can sometimes reach the destination after exploring relatively few cells, but it does **not guarantee the shortest path**.

**Data structure:** Stack

---

### Dijkstra's Algorithm

Dijkstra's Algorithm uses a **priority queue** and tracks the shortest known distance from the starting position to every explored cell.

The next cell with the lowest total distance is explored first.

Since all movements currently have equal cost, Dijkstra often produces the same shortest-path length as BFS.

**Data structure:** Priority Queue (`heapq`)

---

### A* Search

A* improves upon Dijkstra's search by using a **heuristic** to estimate how far each cell is from the destination.

This project uses **Manhattan distance**:

```text
h(n) = |current_row - goal_row| + |current_col - goal_col|
```

A* considers both:

```text
f(n) = g(n) + h(n)
```

where:

- `g(n)` = distance traveled from the start
- `h(n)` = estimated distance to the destination
- `f(n)` = estimated total path cost

This allows A* to direct its search toward the destination rather than exploring equally in every direction.

**Data structure:** Priority Queue (`heapq`)

---

## Random Maze Generation

Each maze is generated using a **randomized recursive backtracking algorithm**.

The maze initially contains walls throughout the grid.

The generator:

1. Begins at the starting cell.
2. Randomly selects an unvisited neighboring cell.
3. Removes the wall between the two cells.
4. Moves to the new cell.
5. Continues until reaching a dead end.
6. Backtracks until another unexplored route is available.
7. Continues until the maze has been generated.

This produces a different maze each time `R` is pressed.

---

## Algorithm Comparison

Pressing `M` runs all four algorithms on the **same maze**, making their performance easier to compare.

The program records:

- Path length
- Number of cells explored
- Execution time

Example:

```text
----------------------------------------
ALGORITHM COMPARISON
----------------------------------------
BFS        | Path: 84 | Explored: 137 | Time: 0.1900 ms
DFS        | Path: 96 | Explored: 103 | Time: 0.1300 ms
Dijkstra   | Path: 84 | Explored: 137 | Time: 0.3100 ms
A*         | Path: 84 | Explored: 101 | Time: 0.2400 ms
----------------------------------------
```

Results vary depending on the randomly generated maze.

BFS, Dijkstra, and A* should generally return the same shortest-path length in the current unweighted maze. DFS may return a longer path because it does not guarantee the shortest solution.

---

## Project Structure

```text
maze-solver-visualizer/
│
├── main.py
├── algorithms.py
├── maze.py
├── visualizer.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Controls the application.

Responsible for:

- Starting Pygame
- Handling keyboard input
- Selecting algorithms
- Running animations
- Managing program state
- Coordinating the other modules

### `algorithms.py`

Contains all pathfinding logic:

- BFS
- DFS
- Dijkstra
- A*
- Neighbor detection
- Path reconstruction
- Performance measurements

### `maze.py`

Handles random maze generation using recursive backtracking.

### `visualizer.py`

Handles Pygame rendering, including:

- Maze walls
- Start and destination cells
- Explored cells
- Final paths
- Algorithm information
- Performance statistics

### `config.py`

Stores shared settings such as:

- Window dimensions
- Grid dimensions
- Colors
- Start and end positions
- Animation speed

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/annan947/maze-solver-visualizer.git
```

### 2. Enter the project directory

```bash
cd maze-solver-visualizer
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The project uses **Pygame Community Edition (`pygame-ce`)**.

### 4. Run the visualizer

```bash
python main.py
```

---

## Technologies Used

- Python
- Pygame Community Edition
- Git
- GitHub

### Python Concepts

- Functions
- Modules and imports
- Lists
- Tuples
- Dictionaries
- Sets
- Queues
- Stacks
- Priority queues
- 2D arrays
- Recursion
- Graph traversal
- Algorithm performance measurement

---

## What I Learned

Building this project helped me develop a better understanding of both software development and data structures and algorithms.

Some of the main concepts I practiced include:

- Structuring a Python project across multiple modules
- Representing a maze as a 2D grid
- Converting grid positions into screen coordinates
- Implementing graph traversal algorithms
- Understanding queues, stacks, and priority queues
- Reconstructing paths using parent relationships
- Using heuristics with A*
- Generating randomized mazes
- Visualizing algorithms with Pygame
- Measuring algorithm performance
- Using Git for version control
- Managing and updating a GitHub repository

---

## Future Improvements

Possible future additions include:

- [x] Random maze generation
- [x] Breadth-First Search
- [x] Depth-First Search
- [x] Dijkstra's Algorithm
- [x] A* Search
- [x] Animated algorithm visualization
- [x] Algorithm performance statistics
- [x] Multi-algorithm comparison
- [ ] Side-by-side algorithm visualization
- [ ] Adjustable animation speed
- [ ] Adjustable maze size
- [ ] Weighted terrain for demonstrating Dijkstra and A*
- [ ] User-selectable start and destination positions
- [ ] Additional maze-generation algorithms
- [ ] Save algorithm benchmark results
- [ ] Improved graphical user interface

---

## Author

**Annan Sharif**

Built as a project to explore pathfinding algorithms, data structures, algorithm visualization, and Python application development.
