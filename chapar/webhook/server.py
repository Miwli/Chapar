"""FastAPI webhook server for receiving GitHub events."""

from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
import hashlib
import hmac
import os

load_dotenv()  

app = FastAPI()


def verify_signature(payload_body: bytes, signature_header: str | None) -> bool:
    """Verify that a webhook request really came from GitHub."""
    secret = os.getenv("GITHUB_WEBHOOK_SECRET", "")

    if not signature_header:
        return False

    expected = "sha256=" + hmac.new(
        secret.encode(), payload_body, hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected, signature_header)


@app.get("/health")
def health_check() -> dict:
    """Simple endpoint to verify the server is running."""
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(request: Request) -> dict:
    """Receive a GitHub webhook event, verify it, and log its payload."""
    body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256")

    if not verify_signature(body, signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    payload = await request.json()
    print(payload)
    return {"received": True}