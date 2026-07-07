# 🏗 NeuroKeys Architecture

```text
                  Camera
                     │
                     ▼
              Vision Engine
                     │
                     ▼
             MediaPipe Hands
                     │
                     ▼
             Finger Tracker
                     │
                     ▼
             Motion Tracker
                     │
                     ▼
              Tap Detector
                     │
                     ▼
           Virtual Keyboard
                     │
                     ▼
             Adaptive AI
```

Each module has a single responsibility, making the project easier to maintain, test, and extend.