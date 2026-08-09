import cv2

from app.camera.stream import CameraStream


def main() -> None:
    with CameraStream(source=0) as stream:
        for frame in stream.frames():
            cv2.imshow("Camera Stream - press 'q' to quit", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()