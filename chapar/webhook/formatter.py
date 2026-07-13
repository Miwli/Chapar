"""Build Telegram message text from internal event models."""

from chapar.core.events import PushEvent


def format_push(event: PushEvent) -> str:
    """Turn a PushEvent into a formatted Telegram message."""
    return (
        f"📦 New push to {event.branch}\n"
        f"👤 {event.author}\n"
        f"🔖 {event.commit_sha}\n"
        f"📝 {event.message}\n"
        f"📊 {event.status}"
    )