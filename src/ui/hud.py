import cv2

from src.ui.theme import (
    PANEL,
    TEXT,
    SUCCESS,
    WARNING,
    SECONDARY_TEXT
)

from src.ui.layout import *


class HUD:
    """
    NeuroKeys Developer HUD

    Displays debugging information while developing.
    """

    def draw(
        self,
        frame,
        index_position,
        movement,
        velocity,
        direction,
        tap
    ):

        x, y = index_position
        dx, dy = movement

        # --------------------------------------------------
        # Background Panel
        # --------------------------------------------------
        cv2.rectangle(
            frame,
            (HUD_X, HUD_Y),
            (
                HUD_X + HUD_WIDTH,
                HUD_Y + HUD_HEIGHT
            ),
            PANEL,
            -1
        )

        # --------------------------------------------------
        # Border
        # --------------------------------------------------
        cv2.rectangle(
            frame,
            (HUD_X, HUD_Y),
            (
                HUD_X + HUD_WIDTH,
                HUD_Y + HUD_HEIGHT
            ),
            SECONDARY_TEXT,
            2
        )

        # --------------------------------------------------
        # Title
        # --------------------------------------------------
        cv2.putText(
            frame,
            "Developer",
            (
                HUD_X + 10,
                HUD_Y + 22
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            SMALL_FONT_SCALE,
            SECONDARY_TEXT,
            TEXT_THICKNESS
        )

        # --------------------------------------------------
        # Index Position
        # --------------------------------------------------
        cv2.putText(
            frame,
            f"Index : ({x}, {y})",
            (
                HUD_X + 10,
                HUD_Y + 50
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            NORMAL_FONT_SCALE,
            SUCCESS,
            TEXT_THICKNESS
        )

        # --------------------------------------------------
        # Movement
        # --------------------------------------------------
        cv2.putText(
            frame,
            f"Move  : ({dx}, {dy})",
            (
                HUD_X + 10,
                HUD_Y + 78
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            NORMAL_FONT_SCALE,
            (255, 255, 0),
            TEXT_THICKNESS
        )

        # --------------------------------------------------
        # Velocity
        # --------------------------------------------------
        cv2.putText(
            frame,
            f"Speed : {velocity:.1f} px/s",
            (
                HUD_X + 10,
                HUD_Y + 106
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            NORMAL_FONT_SCALE,
            WARNING,
            TEXT_THICKNESS
        )

        # --------------------------------------------------
        # Direction
        # --------------------------------------------------
        cv2.putText(
            frame,
            f"Dir   : {direction}",
            (
                HUD_X + 10,
                HUD_Y + 134
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            NORMAL_FONT_SCALE,
            TEXT,
            TEXT_THICKNESS
        )

        # --------------------------------------------------
        # Tap Status
        # --------------------------------------------------
        tap_color = SUCCESS if tap else SECONDARY_TEXT

        cv2.putText(
            frame,
            f"Tap   : {'DETECTED' if tap else 'READY'}",
            (
                HUD_X + 10,
                HUD_Y + 162
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            NORMAL_FONT_SCALE,
            tap_color,
            TEXT_THICKNESS
        )