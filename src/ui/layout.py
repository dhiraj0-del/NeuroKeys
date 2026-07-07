"""
====================================================
NeuroKeys UI Layout
====================================================

This file defines the complete UI layout of NeuroKeys.

All screen positions and dimensions should come from
this file instead of using hardcoded values.

Author: Dhiraj
Project: NeuroKeys
Version: 1.0
"""

# ====================================================
# Window
# ====================================================

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

WINDOW_TITLE = "NeuroKeys Vision Engine"

PADDING = 20

# ====================================================
# Status Bar
# ====================================================

STATUS_BAR_X = 0
STATUS_BAR_Y = 0

STATUS_BAR_WIDTH = WINDOW_WIDTH
STATUS_BAR_HEIGHT = 45

# ====================================================
# Camera Feed Area
# ====================================================

CAMERA_X = 0
CAMERA_Y = STATUS_BAR_HEIGHT

CAMERA_WIDTH = WINDOW_WIDTH
CAMERA_HEIGHT = 360

# ====================================================
# Keyboard Area
# ====================================================

KEYBOARD_X = 10
KEYBOARD_Y = 270

KEYBOARD_WIDTH = WINDOW_WIDTH - 40
KEYBOARD_HEIGHT = 180

# ====================================================
# Typing Panel
# ====================================================

TYPING_PANEL_X = 20

TYPING_PANEL_HEIGHT = 60

BOTTOM_MARGIN = 10

TYPING_PANEL_Y = (
    WINDOW_HEIGHT
    - TYPING_PANEL_HEIGHT
    - BOTTOM_MARGIN
)

TYPING_PANEL_WIDTH = WINDOW_WIDTH - 40

# ====================================================
# HUD (Developer Panel)
# ====================================================

HUD_X = 20

HUD_Y = CAMERA_Y + 20

HUD_WIDTH = 220
HUD_HEIGHT = 180

HUD_LINE_HEIGHT = 28

# ====================================================
# Cursor
# ====================================================

CURSOR_OUTER_RADIUS = 14
CURSOR_INNER_RADIUS = 4

CURSOR_OUTER_THICKNESS = 2

# ====================================================
# Keyboard Keys
# ====================================================

KEY_WIDTH = 38
KEY_HEIGHT = 38

KEY_MARGIN = 5

ROW_INDENT_1 = 0
ROW_INDENT_2 = 20
ROW_INDENT_3 = 40

# ====================================================
# Typography
# ====================================================

TITLE_FONT_SCALE = 0.8
NORMAL_FONT_SCALE = 0.7
SMALL_FONT_SCALE = 0.6

TEXT_THICKNESS = 2

# ====================================================
# Animation
# ====================================================

CURSOR_BLINK_INTERVAL = 0.5

HOVER_DELAY = 0.10

RELEASE_DELAY = 0.10

PRESS_ANIMATION_TIME = 0.10

# ====================================================
# Future Layout
# ====================================================

SHOW_STATUS_BAR = True

SHOW_HUD = True

SHOW_TYPING_PANEL = True

SHOW_KEYBOARD = True