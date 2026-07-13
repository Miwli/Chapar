"""Telegram Bot API for sending notifications."""

import httpx


class TelegramClient:
    def __init__(self, token: str, proxy: str | None = None):
        self._base_url = f"https://api.telegram.org/bot{token}"
        self._client = httpx.Client(trust_env=False, proxy=proxy)

    def send_message(
        self, chat_id: str, text: str, topic_id: int | None = None
    ) -> dict:
        """Send a text message to a chat, optionally into a specific topic."""
        payload = {"chat_id": chat_id, "text": text}

        if topic_id is not None:
            payload["message_thread_id"] = topic_id

        response = self._client.post(f"{self._base_url}/sendMessage", json=payload)
        response.raise_for_status()
        return response.json()