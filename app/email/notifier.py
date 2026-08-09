import smtplib
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path

from app.config.settings import EmailSettings


class EmailNotifier:
    def __init__(self, settings: EmailSettings) -> None:
        self.settings = settings

    def send_alert(self, photo_path: Path, detection_count: int = 1) -> None:
        message = EmailMessage()
        message["Subject"] = "Phone Detector Alert — Unauthorized phone usage detected"
        message["From"] = self.settings.smtp_username
        message["To"] = self.settings.recipient

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = (
            f"A phone was detected in the monitored area.\n\n"
            f"Time: {timestamp}\n"
            f"Detections in frame: {detection_count}\n"
            f"Photo file: {photo_path.name}\n\n"
            f"See the attached photo for visual confirmation."
        )
        message.set_content(body)

        with open(photo_path, "rb") as image_file:
            message.add_attachment(
                image_file.read(),
                maintype="image",
                subtype="jpeg",
                filename=photo_path.name,
            )

        with smtplib.SMTP(self.settings.smtp_host, self.settings.smtp_port) as smtp:
            smtp.starttls()
            smtp.login(self.settings.smtp_username, self.settings.smtp_password)
            smtp.send_message(message)