import cv2

from app.camera.stream import CameraStream
from app.detection.detector import PhoneDetector
from app.storage.capture import DetectionCapture


def main() -> None:
    detector = PhoneDetector()
    capture = DetectionCapture()

    with CameraStream(source=0) as camera:
        for frame in camera.frames():
            result = detector.detect(frame)
            annotated = result.plot()

            if len(result.boxes) > 0:
                saved_path = capture.save(annotated)
                print(f"Phone detected, saved to {saved_path}")

            cv2.imshow("Phone Detection - press 'q' to quit", annotated)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()