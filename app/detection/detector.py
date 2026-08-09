from pathlib import Path

from ultralytics import YOLO
from ultralytics.engine.results import Results

PHONE_CLASS_NAME = "cell phone"


class PhoneDetector:
    def __init__(self, model_path: str = "models/yolov8n.pt", confidence: float = 0.5) -> None:
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame) -> Results:
        results = self.model.predict(
            frame,
            conf=self.confidence,
            classes=self._phone_class_ids(),
            verbose=False,
        )
        return results[0]

    def _phone_class_ids(self) -> list[int]:
        return [
            class_id
            for class_id, name in self.model.names.items()
            if name == PHONE_CLASS_NAME
        ]