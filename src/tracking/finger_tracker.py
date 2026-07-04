class FingerTracker:
    """
    Handles finger landmark access for NeuroKeys.
    """

    # Fingertip landmark IDs
    THUMB_TIP = 4
    INDEX_TIP = 8
    MIDDLE_TIP = 12
    RING_TIP = 16
    PINKY_TIP = 20

    def __init__(self, hand_landmarks):
        self.hand_landmarks = hand_landmarks

        self.previous_x = None
        self.previous_y = None

    def get_thumb_tip(self):
        return self.hand_landmarks.landmark[self.THUMB_TIP]

    def get_index_tip(self):
        return self.hand_landmarks.landmark[self.INDEX_TIP]

    def get_middle_tip(self):
        return self.hand_landmarks.landmark[self.MIDDLE_TIP]

    def get_ring_tip(self):
        return self.hand_landmarks.landmark[self.RING_TIP]

    def get_pinky_tip(self):
        return self.hand_landmarks.landmark[self.PINKY_TIP]