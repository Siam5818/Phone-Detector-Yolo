import cv2

from app.camera.stream import CameraStream
from app.detection.detector import PhoneDetector


def main() -> None:
    detector = PhoneDetector()
    with CameraStream(source=0) as camera:
        for frame in camera.frames():
            result = detector.detect(frame)
            annotated = result.plot()
            cv2.imshow("Phone Detection - press 'q' to quit", annotated)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()