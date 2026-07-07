from src.keyboard.keyboard_layout import KEYBOARD_LAYOUT
from src.keyboard.key import Key

from src.ui.layout import (
    KEYBOARD_X,
    KEYBOARD_Y,
    KEY_WIDTH,
    KEY_HEIGHT,
    KEY_MARGIN,
    ROW_INDENT_1,
    ROW_INDENT_2,
    ROW_INDENT_3,
)


class KeyboardEngine:
    """
    NeuroKeys Keyboard Engine

    Responsibilities
    ----------------
    - Build the virtual keyboard
    - Store key positions
    - Detect hovered key
    """

    def __init__(self):

        # ------------------------------------------
        # Keyboard Layout Settings
        # ------------------------------------------
        self.key_width = KEY_WIDTH
        self.key_height = KEY_HEIGHT
        self.margin = KEY_MARGIN

        self.start_x = KEYBOARD_X
        self.start_y = KEYBOARD_Y

        self.row_offsets = [
            ROW_INDENT_1,
            ROW_INDENT_2,
            ROW_INDENT_3,
        ]

        self.keys = []

        self.build_keyboard()

    def build_keyboard(self):
        """
        Build the keyboard from KEYBOARD_LAYOUT.
        """

        self.keys.clear()

        for row_index, row in enumerate(KEYBOARD_LAYOUT):

            for col_index, label in enumerate(row):

                x = (
                    self.start_x
                    + self.row_offsets[row_index]
                    + col_index * (self.key_width + self.margin)
                )

                y = (
                    self.start_y
                    + row_index * (self.key_height + self.margin)
                )

                self.keys.append(
                    Key(
                        label=label,
                        x=x,
                        y=y,
                        width=self.key_width,
                        height=self.key_height,
                    )
                )

    def get_hovered_key(self, px, py):
        """
        Return the key under the cursor.
        """

        for key in self.keys:

            if key.contains(px, py):
                return key

        return None