from datetime import datetime
from pathlib import Path

import cv2


class DetectionCapture:
    def __init__(self, output_dir: str = "detections") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save(self, annotated_frame) -> Path:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filepath = self.output_dir / f"detection_{timestamp}.jpg"
        cv2.imwrite(str(filepath), annotated_frame)
        return filepath