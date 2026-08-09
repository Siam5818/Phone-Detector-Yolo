import time


class Cooldown:
    def __init__(self, seconds: float = 30.0) -> None:
        self.seconds = seconds
        self._last_trigger: float | None = None

    def is_ready(self) -> bool:
        if self._last_trigger is None:
            return True
        return (time.monotonic() - self._last_trigger) >= self.seconds

    def trigger(self) -> None:
        self._last_trigger = time.monotonic()