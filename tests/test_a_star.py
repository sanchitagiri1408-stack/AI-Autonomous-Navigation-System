import unittest
from src.planning.a_star import find_path, manhattan
from src.simulation.world import create_world, START, GOAL

class AStarTests(unittest.TestCase):
    def test_manhattan(self):
        self.assertEqual(manhattan((0, 0), (3, 4)), 7)

    def test_path_exists_and_reaches_goal(self):
        grid = create_world()
        path = find_path(grid, START, GOAL)
        self.assertTrue(path)
        self.assertEqual(path[0], START)
        self.assertEqual(path[-1], GOAL)

    def test_path_avoids_obstacles(self):
        grid = create_world()
        path = find_path(grid, START, GOAL)
        self.assertTrue(all(not grid[r][c] for r, c in path))

    def test_no_route(self):
        grid = [[False, True, False]]
        self.assertEqual(find_path(grid, (0, 0), (0, 2)), [])

if __name__ == "__main__":
    unittest.main()
