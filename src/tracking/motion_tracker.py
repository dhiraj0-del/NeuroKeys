class MotionTracker:
    """
    Tracks fingertip movement across consecutive frames.
    """

    def __init__(self):
        self.previous_position = None
        self.current_position = None

    def update(self, position):
        """
        Update the current fingertip position.
        """

        self.previous_position = self.current_position
        self.current_position = position

    def get_delta(self):
        """
        Returns movement (dx, dy).
        """

        if self.previous_position is None:
            return (0, 0)

        dx = self.current_position[0] - self.previous_position[0]
        dy = self.current_position[1] - self.previous_position[1]

        return (dx, dy)