import cv2

from src.ui.theme import CURSOR
from src.ui.layout import (
    CURSOR_OUTER_RADIUS,
    CURSOR_INNER_RADIUS,
    CURSOR_OUTER_THICKNESS
)


class Cursor:
    """
    NeuroKeys Cursor

    Draws the fingertip cursor.

    Style:
    - Outer Ring
    - Inner Dot
    """

    def draw(self, frame, x, y):

        # -----------------------------------------
        # Outer Ring
        # -----------------------------------------
        cv2.circle(
            frame,
            (x, y),
            CURSOR_OUTER_RADIUS,
            CURSOR,
            CURSOR_OUTER_THICKNESS
        )

        # -----------------------------------------
        # Inner Dot
        # -----------------------------------------
        cv2.circle(
            frame,
            (x, y),
            CURSOR_INNER_RADIUS,
            CURSOR,
            -1
        )