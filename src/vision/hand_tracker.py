import cv2
import mediapipe as mp

from src.tracking.finger_tracker import FingerTracker
from src.tracking.motion_tracker import MotionTracker
from src.ui.hud import HUD
from src.tracking.tap_detector import TapDetector


class HandTracker:
    """
    NeuroKeys Vision Engine

    Responsibilities:
    - Capture webcam frames
    - Detect hands
    - Track fingertips
    - Track motion
    - Delegate HUD rendering
    """

    def __init__(self):

        # -----------------------------
        # Camera
        # -----------------------------
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Could not open webcam.")

        cv2.namedWindow("NeuroKeys Vision Engine", cv2.WINDOW_NORMAL)

        # -----------------------------
        # MediaPipe
        # -----------------------------
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

        # -----------------------------
        # Tracking Modules
        # -----------------------------
        self.motion_tracker = MotionTracker()

        # -----------------------------
        # UI
        # -----------------------------
        self.hud = HUD()
        
        
        self.tap_detector = TapDetector()

    def run(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                print("Failed to capture frame.")
                break

            frame = cv2.flip(frame, 1)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = self.hands.process(rgb_frame)

            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:

                    # -----------------------------
                    # Finger Tracking
                    # -----------------------------
                    finger_tracker = FingerTracker(hand_landmarks)

                    index_tip = finger_tracker.get_index_tip()

                    frame_height, frame_width = frame.shape[:2]

                    x = int(index_tip.x * frame_width)
                    y = int(index_tip.y * frame_height)

                    # -----------------------------
                    # Motion Tracking
                    # -----------------------------
                    self.motion_tracker.update((x, y))

                    dx, dy = self.motion_tracker.get_delta()

                    velocity = self.motion_tracker.get_velocity()

                    direction = self.motion_tracker.get_direction()
                    
                    tap = self.tap_detector.detect(
                        velocity,
                        direction
                    )

                    # -----------------------------
                    # Debug Console
                    # -----------------------------
                    print(
                        f"x={x}, y={y} | "
                        f"dx={dx}, dy={dy} | "
                        f"velocity={velocity:.2f} px/s | "
                        f"direction={direction}"
                    )

                    # -----------------------------
                    # Draw Skeleton
                    # -----------------------------
                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

                    # -----------------------------
                    # Draw Fingertip
                    # -----------------------------
                    cv2.circle(
                        frame,
                        (x, y),
                        12,
                        (0, 255, 0),
                        -1
                    )

                    # -----------------------------
                    # Draw HUD
                    # -----------------------------
                    self.hud.draw(
                        frame,
                        index_position=(x, y),
                        movement=(dx, dy),
                        velocity=velocity,
                        direction=direction,
                        tap=tap
                    )

            cv2.imshow("NeuroKeys Vision Engine", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.camera.release()
        cv2.destroyAllWindows()