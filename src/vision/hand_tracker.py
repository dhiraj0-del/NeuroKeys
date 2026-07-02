import cv2


class HandTracker:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Could not open webcam")

    def run(self):
        while True:
            success, frame = self.camera.read()

            if not success:
                print("Failed to read frame")
                break
            cv2.namedWindow("NeuroKeys Vision Engine", cv2.WINDOW_NORMAL)
            cv2.imshow("NeuroKeys Vision Engine", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.camera.release()
        cv2.destroyAllWindows()