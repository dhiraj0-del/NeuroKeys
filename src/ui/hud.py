import cv2


class HUD:
    """
    NeuroKeys Debug Heads-Up Display
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

        # -----------------------------
        # Index Finger Position
        # -----------------------------
        cv2.putText(
            frame,
            f"Index: ({x}, {y})",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # -----------------------------
        # Movement
        # -----------------------------
        cv2.putText(
            frame,
            f"Movement: ({dx}, {dy})",
            (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        # -----------------------------
        # Velocity
        # -----------------------------
        cv2.putText(
            frame,
            f"Velocity: {velocity:.1f} px/s",
            (10, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 165, 255),
            2
        )

        # -----------------------------
        # Direction
        # -----------------------------
        cv2.putText(
            frame,
            f"Direction: {direction}",
            (10, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 100, 255),
            2
        )
        
        
        cv2.putText(
            frame,
            f"Tap: {'YES' if tap else 'NO'}",
            (10, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255) if tap else (200, 200, 200),
            2
        )