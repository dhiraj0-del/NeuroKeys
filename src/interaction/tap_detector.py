"""
NeuroKeys Tap Detector

Detects a single tap using
velocity and direction.

One tap -> One event
"""

class TapDetector:

    def __init__(self, velocity_threshold=150):

        self.velocity_threshold = velocity_threshold

        self.ready = True

    def detect(self, velocity, direction):

        # --------------------------
        # Detect Tap
        # --------------------------
        if (
            self.ready
            and direction == "Down"
            and velocity > self.velocity_threshold
        ):

            self.ready = False

            return True

        # --------------------------
        # Reset
        # --------------------------
        if velocity < 15:

            self.ready = True

        return False