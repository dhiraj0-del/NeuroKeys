class TapDetector:
    """
    Detects tap gestures based on finger movement.
    """

    def __init__(self, velocity_threshold=150):
        self.velocity_threshold = velocity_threshold
        self.tap_detected = False

    def detect(self, velocity, direction):
        """
        Returns True if a tap gesture is detected.
        """

        if (
            direction == "Down"
            and velocity > self.velocity_threshold
        ):
            self.tap_detected = True
        else:
            self.tap_detected = False

        return self.tap_detected