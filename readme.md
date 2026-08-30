# Maze Solver Visualizer

An interactive maze generation and pathfinding visualizer built with **Python** and **Pygame**.

The program automatically generates a random maze using a recursive backtracking algorithm and uses **Breadth-First Search (BFS)** to find the shortest path from the starting cell to the destination.

The search process is animated so users can visualize how BFS explores the maze before displaying the final shortest path.

## Features

- Random maze generation
- Recursive backtracking maze-generation algorithm
- Breadth-First Search (BFS) pathfinding
- Animated visualization of BFS exploration
- Shortest-path reconstruction
- Generate new mazes without restarting the program
- Clear and rerun pathfinding visualization
- Displays path length and number of explored cells

## Controls

| Key | Action |
| --- | --- |
| `SPACE` | Run BFS and solve the maze |
| `R` | Generate a new random maze |
| `C` | Clear the current solution |
| `X` / Close Window | Exit the program |

## How It Works

### 1. Maze Generation

The maze begins as a grid filled entirely with walls.

A **recursive backtracking algorithm** then carves passages through the grid. The algorithm explores random neighboring cells and backtracks whenever it reaches a dead end.

This creates a connected maze with a valid route through it.

### 2. Breadth-First Search

After the maze is generated, BFS searches for a path between the green starting cell and the red destination.

BFS uses a queue to explore cells in layers:

1. Begin at the starting cell.
2. Add neighboring open cells to the queue.
3. Keep track of visited cells.
4. Continue exploring until the destination is reached.
5. Use each cell's recorded parent to reconstruct the shortest path.

Because every movement in the maze has the same cost, BFS guarantees a shortest path.

## Visualization

The maze uses different colors to represent the state of the algorithm:

- 🟢 **Green** — Starting position
- 🔴 **Red** — Destination
- 🟣 **Purple** — Cells explored by BFS
- 🔵 **Blue** — Shortest path
- ⬜ **White/Gray** — Walls

## Technologies

- Python
- Pygame / Pygame Community Edition
- `collections.deque`
- Randomized maze generation
- Graph traversal algorithms

## Installation

Clone the repository:

```bash
git clone YOUR-GITHUB-REPOSITORY-URL
