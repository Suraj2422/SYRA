import cv2
import numpy as np


class ActivityAnalyzer:
    def __init__(self):
        self.prev_frame = None

    def analyze(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if self.prev_frame is None:
            self.prev_frame = gray
            return {
                "activity": "initializing",
                "change": 0.0
            }

        # Frame difference (motion / change detection)
        diff = cv2.absdiff(self.prev_frame, gray)
        change_score = np.mean(diff)

        self.prev_frame = gray

        # Simple interpretation
        if change_score < 2:
            activity = "idle"
        elif change_score < 10:
            activity = "low activity"
        else:
            activity = "high activity"

        return {
            "activity": activity,
            "change": round(float(change_score), 2)
        }
