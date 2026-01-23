import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WebhookClient:
    def __init__(self):
        self.process_analyzed_url = os.getenv(
            "N8N_PROCESS_ANALYZED_WEBHOOK_URL"
        )
        self.process_created_url = os.getenv(
            "N8N_PROCESS_CREATED_WEBHOOK_URL"
        )

        if not self.process_analyzed_url:
            raise ValueError("N8N_PROCESS_ANALYZED_WEBHOOK_URL not configured")

        if not self.process_created_url:
            raise ValueError("N8N_PROCESS_CREATED_WEBHOOK_URL not configured")

    def send_process_analysis(self, payload: dict) -> None:
        response = requests.post(
            self.process_analyzed_url,
            json=payload,
            timeout=10
        )
        response.raise_for_status()

    def send_process_created(self, payload: dict) -> None:
        response = requests.post(
            self.process_created_url,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
