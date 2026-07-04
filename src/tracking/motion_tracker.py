class MotionTracker:
    """
    Tracks fingertip movement across consecutive frames.

    Responsibilities:
    - Store previous position
    - Store current position
    - Calculate movement
    - Calculate velocity
    - Determine direction
    """

    def __init__(self):
        self.previous_position = None
        self.current_position = None