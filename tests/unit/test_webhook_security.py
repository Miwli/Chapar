"""Tests for webhook signature verification."""

import hashlib
import hmac

from chapar.webhook.server import verify_signature


def test_valid_signature_is_accepted(monkeypatch):
    monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", "test-secret")

    body = b'{"test": "data"}'
    signature = "sha256=" + hmac.new(b"test-secret", body, hashlib.sha256).hexdigest()

    assert verify_signature(body, signature) is True


def test_invalid_signature_is_rejected(monkeypatch):
    monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", "test-secret")

    body = b'{"test": "data"}'

    assert verify_signature(body, "sha256=wrong") is False


def test_missing_signature_is_rejected(monkeypatch):
    monkeypatch.setenv("GITHUB_WEBHOOK_SECRET", "test-secret")

    body = b'{"test": "data"}'

    assert verify_signature(body, None) is False