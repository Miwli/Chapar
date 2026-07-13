"""Internal event models decoupled from raw webhook payloads."""

from dataclasses import dataclass


@dataclass
class PushEvent:
    author: str
    branch: str
    commit_sha: str
    message: str
    status: str