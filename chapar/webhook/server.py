"""FastAPI webhook server for receiving GitHub events."""

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/health")
def health_check() -> dict:
    """Simple endpoint to verify the server is running."""
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(request: Request) -> dict:
    """Receive a GitHub webhook event and log its payload."""
    payload = await request.json()
    print(payload)
    return {"received": True}