# Architecture

```text
Known occupancy grid + start + goal
                |
                v
      World representation
                |
                v
       A* path planner
                |
                v
     Ordered waypoint list
                |
                v
   Waypoint-following controller
                |
                v
     Simulated robot movement
                |
                v
 Collision guard + run metrics
                |
                v
     Pygame visualization/output
```

## Current scope
This version plans against a known static occupancy grid. It does not use a camera, trained object detector, SLAM, vehicle dynamics, or real hardware. The yellow circle is a simulated robot and its movement is a simple waypoint follower.
