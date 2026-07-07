"""
NeuroKeys Motion Tracker

Tracks fingertip movement across consecutive frames.

Responsibilities:
- Store previous and current fingertip positions
- Calculate movement (dx, dy)
- Calculate movement speed
- Determine movement direction
"""

import math
import time


class MotionTracker:

    def __init__(self):
        """
        Initialize the motion tracker.
        """

        self.previous_position = None
        self.current_position = None

        self.previous_time = None
        self.current_time = None

    def update(self, position):
        """
            Update fingertip position and timestamp.
        """

        self.previous_position = self.current_position
        self.previous_time = self.current_time

        self.current_position = position
        self.current_time = time.time()

    def get_delta(self):
        """
        Returns
        -------
        tuple
            (dx, dy)
        """

        if self.previous_position is None:
            return (0, 0)

        dx = self.current_position[0] - self.previous_position[0]
        dy = self.current_position[1] - self.previous_position[1]

        return (dx, dy)
    
    def get_velocity(self):
        """
        Returns fingertip velocity in pixels per second.
        """

        if self.previous_time is None:
            return 0.0

        delta_time = self.current_time - self.previous_time

        if delta_time <= 0:
            return 0.0

        dx, dy = self.get_delta()

        distance = math.sqrt(dx**2 + dy**2)

        velocity = distance / delta_time

        return velocity

    def get_speed(self):
        """
        Returns the movement speed in pixels per frame.
        """

        dx, dy = self.get_delta()

        speed = math.sqrt(dx ** 2 + dy ** 2)

        return speed

    def get_direction(self):
        """
        Determine the movement direction.

        Returns
        -------
        str
        """

        dx, dy = self.get_delta()

        threshold = 5

        if abs(dx) < threshold and abs(dy) < threshold:
            return "Stationary"

        if abs(dx) > abs(dy):

            if dx > 0:
                return "Right"

            return "Left"

        else:

            if dy > 0:
                return "Down"

            return "Up"

    def reset(self):
        """
        Reset motion history.
        """

        self.previous_position = None
        self.current_position = None