import cv2
import time

from src.ui.theme import PANEL, TEXT, SECONDARY_TEXT
from src.ui.layout import *


class TypingPanel:
    """
    NeuroKeys Typing Panel

    Displays:
    - Typed Text
    - Blinking Cursor
    """

    def __init__(self):

        self.cursor_visible = True
        self.last_toggle = time.time()

    def draw(self, frame, text):

        # -------------------------------------------------
        # Cursor Blink
        # -------------------------------------------------
        current_time = time.time()

        if current_time - self.last_toggle >= CURSOR_BLINK_INTERVAL:

            self.cursor_visible = not self.cursor_visible
            self.last_toggle = current_time

        display_text = text

        if self.cursor_visible:
            display_text += "|"

        # -------------------------------------------------
        # Panel Background
        # -------------------------------------------------
        cv2.rectangle(
            frame,
            (TYPING_PANEL_X, TYPING_PANEL_Y),
            (
                TYPING_PANEL_X + TYPING_PANEL_WIDTH,
                TYPING_PANEL_Y + TYPING_PANEL_HEIGHT
            ),
            PANEL,
            -1
        )

        # -------------------------------------------------
        # Border
        # -------------------------------------------------
        cv2.rectangle(
            frame,
            (TYPING_PANEL_X, TYPING_PANEL_Y),
            (
                TYPING_PANEL_X + TYPING_PANEL_WIDTH,
                TYPING_PANEL_Y + TYPING_PANEL_HEIGHT
            ),
            SECONDARY_TEXT,
            2
        )

        # -------------------------------------------------
        # Title
        # -------------------------------------------------
        cv2.putText(
            frame,
            "Typing",
            (
                TYPING_PANEL_X + 15,
                TYPING_PANEL_Y + 22
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            SMALL_FONT_SCALE,
            SECONDARY_TEXT,
            TEXT_THICKNESS
        )

        # -------------------------------------------------
        # Typed Text
        # -------------------------------------------------
        cv2.putText(
            frame,
            display_text,
            (
                TYPING_PANEL_X + 15,
                TYPING_PANEL_Y + 55
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            NORMAL_FONT_SCALE,
            TEXT,
            TEXT_THICKNESS
        )