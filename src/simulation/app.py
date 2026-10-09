"""Pygame visualization and simple waypoint-following controller."""
import os
import json
import math
import pygame
from src.planning.a_star import find_path
from src.simulation.world import ROWS, COLS, START, GOAL, create_world

CELL = 28
PANEL = 270
WIDTH, HEIGHT = COLS * CELL + PANEL, ROWS * CELL
FPS = 60

def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AI-Based Autonomous Navigation System")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 17)
    small = pygame.font.SysFont("consolas", 14)

    grid = create_world()
    path = find_path(grid, START, GOAL)
    if not path:
        print("ERROR: No route found. Check the map and start/goal cells.")
        pygame.quit()
        return

    robot_x = START[1] * CELL + CELL / 2
    robot_y = START[0] * CELL + CELL / 2
    waypoint_index = 1
    speed = 105.0  # pixels/second
    running = True
    paused = False
    finished = False
    collision = False
    start_ticks = pygame.time.get_ticks()
    elapsed = 0.0

    def center(cell):
        return cell[1] * CELL + CELL / 2, cell[0] * CELL + CELL / 2

    while running:
        dt = min(clock.tick(FPS) / 1000.0, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    robot_x, robot_y = center(START)
                    waypoint_index = 1
                    finished = collision = paused = False
                    elapsed = 0.0
                    start_ticks = pygame.time.get_ticks()
                elif event.key == pygame.K_s:
                    os.makedirs("outputs", exist_ok=True)
                    pygame.image.save(screen, "outputs/navigation_screenshot.png")
                    with open("outputs/run_summary.json", "w", encoding="utf-8") as f:
                        json.dump({
                            "status": "success" if finished and not collision else "incomplete",
                            "path_cells": len(path),
                            "path_length_grid_steps": max(0, len(path)-1),
                            "collision_detected": collision,
                            "elapsed_seconds": round(elapsed, 2)
                        }, f, indent=2)
                    print("Saved outputs/navigation_screenshot.png and outputs/run_summary.json")

        if not paused and not finished and not collision:
            elapsed = (pygame.time.get_ticks() - start_ticks) / 1000.0
            if waypoint_index < len(path):
                target_x, target_y = center(path[waypoint_index])
                dx, dy = target_x - robot_x, target_y - robot_y
                distance = math.hypot(dx, dy)
                step = speed * dt
                if distance <= step:
                    robot_x, robot_y = target_x, target_y
                    waypoint_index += 1
                elif distance > 0:
                    robot_x += dx / distance * step
                    robot_y += dy / distance * step
            else:
                finished = True

            # Safety guard: robot centre must remain in a free cell.
            col = int(robot_x // CELL)
            row = int(robot_y // CELL)
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col]:
                collision = True

        screen.fill((20, 24, 32))
        # Draw grid and occupancy map.
        for r in range(ROWS):
            for c in range(COLS):
                rect = pygame.Rect(c*CELL, r*CELL, CELL-1, CELL-1)
                color = (49, 56, 67) if grid[r][c] else (232, 237, 242)
                pygame.draw.rect(screen, color, rect)
        # Planned route
        if len(path) > 1:
            points = [center(p) for p in path]
            pygame.draw.lines(screen, (40, 155, 220), False, points, 4)
        # Start and goal
        pygame.draw.circle(screen, (40, 170, 90), center(START), 10)
        pygame.draw.circle(screen, (225, 70, 70), center(GOAL), 10)
        # Robot
        pygame.draw.circle(screen, (255, 190, 40), (int(robot_x), int(robot_y)), 9)
        pygame.draw.circle(screen, (35, 35, 35), (int(robot_x), int(robot_y)), 9, 2)

        panel_x = COLS * CELL
        pygame.draw.rect(screen, (30, 36, 47), (panel_x, 0, PANEL, HEIGHT))
        lines = [
            ("AUTONOMOUS NAVIGATION", (255,255,255)),
            ("", (255,255,255)),
            ("Planner: A* search", (180,220,255)),
            (f"Route cells: {len(path)}", (255,255,255)),
            (f"Grid steps: {len(path)-1}", (255,255,255)),
            (f"Elapsed: {elapsed:.1f}s", (255,255,255)),
            ("", (255,255,255)),
            ("STATUS", (255,255,255)),
            ("COLLISION!" if collision else "GOAL REACHED" if finished else "PAUSED" if paused else "NAVIGATING",
             (255,90,90) if collision else (90,230,140)),
            ("", (255,255,255)),
            ("CONTROLS", (255,255,255)),
            ("SPACE  pause/resume", (220,220,220)),
            ("R      reset run", (220,220,220)),
            ("S      save screenshot", (220,220,220)),
            ("ESC    quit", (220,220,220)),
            ("", (255,255,255)),
            ("Legend", (255,255,255)),
            ("Green: start", (90,230,140)),
            ("Red: goal", (255,100,100)),
            ("Yellow: robot", (255,200,60)),
            ("Blue: planned route", (80,180,240)),
            ("Dark: obstacle", (180,180,180)),
            ("", (255,255,255)),
            ("Model: known grid map", (190,190,190)),
            ("Not camera perception", (190,190,190)),
        ]
        y = 20
        for label, color in lines:
            if label:
                screen.blit(font.render(label, True, color), (panel_x + 14, y))
            y += 25 if label else 12
        pygame.display.flip()

    pygame.quit()
