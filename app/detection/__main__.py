import cv2

from app.camera.stream import CameraStream
from app.config.cooldown import Cooldown
from app.config.settings import EmailSettings
from app.detection.detector import PhoneDetector
from app.email.notifier import EmailNotifier
from app.storage.capture import DetectionCapture


def main() -> None:
    detector = PhoneDetector()
    capture = DetectionCapture()
    cooldown = Cooldown(seconds=30.0)
    notifier = EmailNotifier(EmailSettings.from_env())

    with CameraStream(source=0) as camera:
        for frame in camera.frames():
            result = detector.detect(frame)
            annotated = result.plot()

            if len(result.boxes) > 0 and cooldown.is_ready():
                saved_path = capture.save(annotated)
                cooldown.trigger()
                notifier.send_alert(saved_path, detection_count=len(result.boxes))
                print(f"Phone detected, alert sent for {saved_path}")

            cv2.imshow("Phone Detection - press 'q' to quit", annotated)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()