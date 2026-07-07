import cv2

from src.ui.theme import *
from src.ui.layout import *


class StatusBar:
    """
    NeuroKeys Status Bar

    Displays:
    - Application Title
    - Camera Status
    - Tracking Status
    - FPS
    """

    def draw(self, frame, fps=30):

        # ------------------------------------------------
        # Background
        # ------------------------------------------------
        cv2.rectangle(
            frame,
            (STATUS_BAR_X, STATUS_BAR_Y),
            (
                STATUS_BAR_X + STATUS_BAR_WIDTH,
                STATUS_BAR_Y + STATUS_BAR_HEIGHT
            ),
            PANEL,
            -1
        )

        # ------------------------------------------------
        # Application Title
        # ------------------------------------------------
        cv2.putText(
            frame,
            "NeuroKeys v1.0",
            (
                STATUS_BAR_X + 15,
                STATUS_BAR_Y + 30
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            TITLE_FONT_SCALE,
            TEXT,
            TEXT_THICKNESS
        )

        # ------------------------------------------------
        # Camera Status
        # ------------------------------------------------
        cv2.putText(
            frame,
            "🟢 Camera",
            (
                STATUS_BAR_X + 300,
                STATUS_BAR_Y + 30
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            SMALL_FONT_SCALE,
            SUCCESS,
            TEXT_THICKNESS
        )

        # ------------------------------------------------
        # Tracking Status
        # ------------------------------------------------
        cv2.putText(
            frame,
            "🟢 Tracking",
            (
                STATUS_BAR_X + 470,
                STATUS_BAR_Y + 30
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            SMALL_FONT_SCALE,
            SUCCESS,
            TEXT_THICKNESS
        )

        # ------------------------------------------------
        # FPS
        # ------------------------------------------------
        cv2.putText(
            frame,
            f"{fps:.0f} FPS",
            (
                STATUS_BAR_WIDTH - 140,
                STATUS_BAR_Y + 30
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            SMALL_FONT_SCALE,
            TEXT,
            TEXT_THICKNESS
        )