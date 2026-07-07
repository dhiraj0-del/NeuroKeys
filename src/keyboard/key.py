class Key:
    """
    Represents a single virtual key.
    """

    def __init__(self, label, x, y, width, height):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def contains(self, px, py):
        return (
            self.x <= px <= self.x + self.width
            and
            self.y <= py <= self.y + self.height
        )