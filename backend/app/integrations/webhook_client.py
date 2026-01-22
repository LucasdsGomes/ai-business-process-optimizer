import os
import requests
from dotenv import load_dotenv
load_dotenv()

class WebhookClient:
    def __init__(self):
        self.url = os.getenv("AUTOMATION_WEBHOOK_URL")
        print(f"Webhook URL: {self.url}")

        if not self.url:
            raise RuntimeError("AUTOMATION_WEBHOOK_URL não definida")

    def send(self, payload: dict):
        response = requests.post(
            self.url,
            json=payload,
            timeout=10
        )

        response.raise_for_status()
        return response
