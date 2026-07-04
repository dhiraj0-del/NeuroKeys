import cv2
import mediapipe as mp
from src.tracking.finger_tracker import FingerTracker


class HandTracker:
    def __init__(self):
        # Initialize Camera
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Could not open webcam.")

        # Create Window
        cv2.namedWindow("NeuroKeys Vision Engine", cv2.WINDOW_NORMAL)

        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        # Drawing Utility
        self.mp_draw = mp.solutions.drawing_utils

    def run(self):

        while True:

            success, frame = self.camera.read()

            if not success:
                print("Failed to capture frame.")
                break

            # Flip image for mirror view
            frame = cv2.flip(frame, 1)

            # Convert BGR → RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # AI Processing
            results = self.hands.process(rgb_frame)

            # Draw landmarks
            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:
                    finger_tracker = FingerTracker(hand_landmarks)
                    index_tip = finger_tracker.get_index_tip()
                    height, width, _ = frame.shape

                    x = int(index_tip.x * width)
                    y = int(index_tip.y * height)

                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )
                    cv2.circle(
                        frame,
                        (x, y),
                        12,
                        (0, 255, 0),
                        -1
                    )
                    cv2.putText(
                        frame,
                        f"Index: ({x}, {y})",
                        (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2
                    )

            cv2.imshow("NeuroKeys Vision Engine", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()