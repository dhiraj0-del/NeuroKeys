"""
NeuroKeys Hover Manager

Responsible for:
- Hover confirmation delay
- Hover persistence
- Stable key selection
"""

import time


class HoverManager:

    def __init__(
        self,
        hover_delay=0.10,      # 100 ms
        release_delay=0.10     # 100 ms
    ):

        self.hover_delay = hover_delay
        self.release_delay = release_delay

        self.current_key = None
        self.confirmed_key = None

        self.enter_time = 0
        self.leave_time = 0

    def update(self, hovered_key):

        now = time.time()

        # -----------------------------------
        # Finger entered a different key
        # -----------------------------------
        if hovered_key != self.current_key:

            self.current_key = hovered_key
            self.enter_time = now

        # -----------------------------------
        # Confirm hover after delay
        # -----------------------------------
        if (
            hovered_key is not None
            and hovered_key == self.current_key
        ):

            if now - self.enter_time >= self.hover_delay:
                self.confirmed_key = hovered_key

        # -----------------------------------
        # Finger left all keys
        # -----------------------------------
        if hovered_key is None:

            if self.leave_time == 0:
                self.leave_time = now

            if now - self.leave_time >= self.release_delay:
                self.confirmed_key = None

        else:
            self.leave_time = 0

        return self.confirmed_key