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


class MotionTracker:

    def __init__(self):
        """
        Initialize the motion tracker.
        """

        self.previous_position = None
        self.current_position = None

    def update(self, position):
        """
        Update the fingertip position.

        Parameters
        ----------
        position : tuple
            (x, y) coordinates of the fingertip.
        """

        self.previous_position = self.current_position
        self.current_position = position

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