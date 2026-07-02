from src.vision.hand_tracker import HandTracker


def main():
    tracker = HandTracker()
    tracker.run()


if __name__ == "__main__":
    main()