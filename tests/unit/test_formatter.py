"""Tests for the push event formatter."""

from chapar.core.events import PushEvent
from chapar.webhook.formatter import format_push


def test_format_push_includes_all_fields():
    event = PushEvent(
        author="testuser",
        branch="main",
        commit_sha="abc1234",
        message="add example feature",
        status="success",
    )

    result = format_push(event)

    assert "testuser" in result
    assert "main" in result
    assert "abc1234" in result
    assert "add example feature" in result
    assert "success" in result