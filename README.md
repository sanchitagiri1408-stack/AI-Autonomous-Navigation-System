# AI-Based Autonomous Navigation System

A beginner-friendly 2D autonomous navigation simulation built with Python and Pygame. It represents the world as an occupancy grid, computes a route with A* search, follows waypoints, checks for collisions, and visualizes the run.

> **Scope note:** This is a virtual grid-world prototype. It does not yet implement camera-based AI perception, a trained object detector, SLAM, realistic vehicle physics, or real-robot control.

## Features
- 2D virtual environment with walls and obstacles
- A* path planning with Manhattan-distance heuristic
- Simulated waypoint-following robot
- Basic collision guard
- Live route and status visualization
- Save a screenshot and JSON run summary
- Unit tests for planner behavior

## Tech stack
- Python 3.10–3.12 recommended
- Pygame for simulation display
- Standard-library `heapq` for the A* priority queue
- `unittest` for tests

## Architecture
See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Setup

### Windows PowerShell
```powershell
python --version
mkdir AI-Autonomous-Navigation-System
cd AI-Autonomous-Navigation-System
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run this for the current terminal only:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run
From the repository root, with the virtual environment activated:
```bash
python main.py
```

Controls:
- `SPACE`: pause/resume
- `R`: reset the run
- `S`: save the current view and run summary
- `ESC`: exit

After pressing `S`, the app writes `outputs/navigation_screenshot.png` and `outputs/run_summary.json`.

## Tests
```bash
python -m unittest discover -s tests -v
```

## How it works
1. `create_world()` builds an occupancy grid (`True` = obstacle).
2. `find_path()` searches the grid using A*.
3. A waypoint follower moves the simulated robot along the path.
4. A safety guard checks whether the robot enters an occupied cell.
5. Pygame displays the map, route, robot, status, and run metrics.

A* evaluates nodes using `f(n) = g(n) + h(n)`, where `g(n)` is the known cost from the start and `h(n)` is the Manhattan-distance estimate to the goal. With four-direction movement and uniform costs, this heuristic is appropriate for the grid.

## Results
When the project runs correctly, the robot starts at the green marker, follows the blue route, and reaches the red goal without entering obstacle cells. Press `S` to save evidence. Do not claim numerical performance results until you run and measure them.

## Screenshots and demo
Add your captured evidence to `images/` and `videos/`. Example README embeds:
```markdown
![Navigation simulation](images/navigation-success.png)
```
A short MP4 can be linked from the repository or hosted externally. Keep repository files reasonably small.

## Folder structure
```text
AI-Autonomous-Navigation-System/
├── src/
│   ├── planning/a_star.py
│   └── simulation/{world.py, app.py}
├── tests/test_a_star.py
├── docs/ARCHITECTURE.md
├── images/
├── videos/
├── outputs/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Limitations and future work
- Add a camera/image-based perception module using OpenCV.
- Add a lightweight object detector only after the baseline is stable.
- Add moving obstacles and replanning.
- Compare A* with Dijkstra and BFS.
- Add metrics such as path length, planning time, explored nodes, and success rate.
- Explore ROS 2 and Gazebo/Webots; explore CARLA for vehicle-focused simulation.
- Add localization noise, realistic motion constraints, and automated scenario tests.

## Learning outcomes
- Grid/world representation
- A* path planning and heuristics
- Waypoint-following control
- Simulation loops and visualization
- Unit testing and reproducible project documentation
- Git and GitHub portfolio workflow

## Author
**Your Name** — Student project for learning autonomous navigation and robotics fundamentals.

## 🎥 Project Demo

[▶️ Watch Robot Simulation Demo](demo/robot-simulation-demo.mp4)

## 🚀 Features Demonstrated
- A* pathfinding algorithm
- Obstacle avoidance
- Autonomous robot navigation
- Goal detection and route planning

## 🛠️ Technologies Used
- Python
- Pygame
- Git and GitHub
