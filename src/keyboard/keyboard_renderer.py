import cv2

from src.ui.theme import (
    KEY_NORMAL,
    KEY_HOVER,
    TEXT,
    PANEL
)

from src.ui.layout import (
    NORMAL_FONT_SCALE,
    TEXT_THICKNESS
)


class KeyboardRenderer:
    """
    NeuroKeys Keyboard Renderer

    Responsibilities
    ----------------
    - Draw virtual keyboard
    - Highlight hovered key
    """

    def draw(self, frame, keys, hovered_key=None):

        for key in keys:

            # ----------------------------------------
            # Default Appearance
            # ----------------------------------------
            fill_color = PANEL
            border_color = KEY_NORMAL
            text_color = TEXT
            border_thickness = 2

            # ----------------------------------------
            # Hover Appearance
            # ----------------------------------------
            if hovered_key == key:

                fill_color = KEY_HOVER
                border_color = KEY_HOVER
                text_color = (0, 0, 0)
                border_thickness = 3

            # ----------------------------------------
            # Key Background
            # ----------------------------------------
            cv2.rectangle(
                frame,
                (key.x, key.y),
                (key.x + key.width, key.y + key.height),
                fill_color,
                -1
            )

            # ----------------------------------------
            # Key Border
            # ----------------------------------------
            cv2.rectangle(
                frame,
                (key.x, key.y),
                (key.x + key.width, key.y + key.height),
                border_color,
                border_thickness
            )

            # ----------------------------------------
            # Calculate Text Position
            # ----------------------------------------
            text_size = cv2.getTextSize(
                key.label,
                cv2.FONT_HERSHEY_SIMPLEX,
                NORMAL_FONT_SCALE,
                TEXT_THICKNESS
            )[0]

            text_x = key.x + (key.width - text_size[0]) // 2
            text_y = key.y + (key.height + text_size[1]) // 2

            # ----------------------------------------
            # Draw Label
            # ----------------------------------------
            cv2.putText(
                frame,
                key.label,
                (text_x, text_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                NORMAL_FONT_SCALE,
                text_color,
                TEXT_THICKNESS
            )