import cv2
import mediapipe as mp

from src.tracking.finger_tracker import FingerTracker
from src.tracking.motion_tracker import MotionTracker

from src.interaction.tap_detector import TapDetector
from src.interaction.hover_manager import HoverManager

from src.keyboard.keyboard_engine import KeyboardEngine
from src.keyboard.keyboard_renderer import KeyboardRenderer

from src.typing.text_buffer import TextBuffer

from src.ui.hud import HUD
from src.ui.status_bar import StatusBar
from src.ui.cursor import Cursor
from src.ui.typing_panel import TypingPanel
from src.ui.layout import *


class HandTracker:
    """
    NeuroKeys Vision Engine

    Responsibilities
    ----------------
    - Capture webcam frames
    - Detect hands
    - Track fingertips
    - Track motion
    - Detect tap gestures
    - Detect hovered keys
    - Render UI
    """

    def __init__(self):

        # -------------------------------------------------
        # Camera
        # -------------------------------------------------
        self.camera = cv2.VideoCapture(0)

        

        print("Width :", self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        print("Height:", self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        

        if not self.camera.isOpened():
            raise Exception("Could not open webcam.")
        
        cv2.namedWindow(WINDOW_TITLE, cv2.WINDOW_NORMAL)

        # -------------------------------------------------
        # MediaPipe
        # -------------------------------------------------
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

        # -------------------------------------------------
        # Tracking
        # -------------------------------------------------
        self.motion_tracker = MotionTracker()
        self.tap_detector = TapDetector()
        self.hover_manager = HoverManager()

        # -------------------------------------------------
        # Keyboard
        # -------------------------------------------------
        self.keyboard_engine = KeyboardEngine()
        self.keyboard_renderer = KeyboardRenderer()

        # -------------------------------------------------
        # Typing
        # -------------------------------------------------
        self.text_buffer = TextBuffer()

        # -------------------------------------------------
        # UI
        # -------------------------------------------------
        self.status_bar = StatusBar()
        self.typing_panel = TypingPanel()
        self.cursor = Cursor()
        self.hud = HUD()

        # -------------------------------------------------
        # Application
        # -------------------------------------------------
        self.debug_mode = True

    def run(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                print("Failed to capture frame.")
                break

            # ---------------------------------------------
            # Mirror Camera
            # ---------------------------------------------
            frame = cv2.flip(frame, 1)

            # ---------------------------------------------
            # Default Values
            # ---------------------------------------------
            hovered_key = None

            x, y = 0, 0
            dx, dy = 0, 0

            velocity = 0
            direction = "None"

            tap = False

            # ---------------------------------------------
            # MediaPipe Processing
            # ---------------------------------------------
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = self.hands.process(rgb_frame)

            # ---------------------------------------------
            # Hand Detection
            # ---------------------------------------------
            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:

                    # Finger Tracking
                    finger_tracker = FingerTracker(hand_landmarks)

                    index_tip = finger_tracker.get_index_tip()

                    frame_height, frame_width = frame.shape[:2]

                    x = int(index_tip.x * frame_width)
                    y = int(index_tip.y * frame_height)

                    # Motion Tracking
                    self.motion_tracker.update((x, y))

                    dx, dy = self.motion_tracker.get_delta()

                    velocity = self.motion_tracker.get_velocity()

                    direction = self.motion_tracker.get_direction()

                    # Tap Detection
                    tap = self.tap_detector.detect(
                        velocity,
                        direction
                    )

                    # Hover Detection
                    raw_hovered_key = self.keyboard_engine.get_hovered_key(
                        x,
                        y
                    )

                    hovered_key = self.hover_manager.update(
                        raw_hovered_key
                    )

                    # Typing
                    if tap and hovered_key is not None:

                        self.text_buffer.add_character(
                            hovered_key.label
                        )

                        if self.debug_mode:
                            print(f"Typed: {hovered_key.label}")

                    # Debug Console
                    if self.debug_mode:

                        if hovered_key:

                            print(
                                f"x={x}, y={y} | "
                                f"Key={hovered_key.label} | "
                                f"Velocity={velocity:.2f} | "
                                f"Direction={direction}"
                            )

                        else:

                            print(
                                f"x={x}, y={y} | "
                                f"Velocity={velocity:.2f} | "
                                f"Direction={direction}"
                            )

                    # Draw Hand Skeleton
                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

                    # Draw Cursor
                    self.cursor.draw(frame, x, y)

            # =================================================
            # Draw UI (ONLY ONCE PER FRAME)
            # =================================================

            # Status Bar
            self.status_bar.draw(frame)

            # Keyboard
            self.keyboard_renderer.draw(
                frame,
                self.keyboard_engine.keys,
                hovered_key
            )

            # Typing Panel
            self.typing_panel.draw(
                frame,
                self.text_buffer.get_text()
            )

            # HUD
            if self.debug_mode:

                self.hud.draw(
                    frame,
                    index_position=(x, y),
                    movement=(dx, dy),
                    velocity=velocity,
                    direction=direction,
                    tap=tap
                )

            # =================================================
            # Display
            # =================================================

            cv2.imshow(
                WINDOW_TITLE,
                frame
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.camera.release()
        cv2.destroyAllWindows()