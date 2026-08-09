import cv2
from collections.abc import Generator


class CameraStream:
    """Wraps cv2.VideoCapture as a context manager that yields frames."""

    def __init__(self, source: int | str = 0) -> None:
        self.source = source
        self._capture: cv2.VideoCapture | None = None

    def __enter__(self) -> "CameraStream":
        self._capture = cv2.VideoCapture(self.source, cv2.CAP_DSHOW)
        if not self._capture.isOpened():
            raise RuntimeError(f"Unable to open camera source: {self.source}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._capture is not None:
            self._capture.release()

    def frames(self) -> Generator[cv2.typing.MatLike, None, None]:
        if self._capture is None:
            raise RuntimeError("CameraStream must be used as a context manager")
        while True:
            success, frame = self._capture.read()
            if not success:
                break
            yield frame