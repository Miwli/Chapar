"""Configuration schema for Chapar, validated using Pydantic."""

from pydantic import BaseModel

class TelegramConfig(BaseModel):
    bot_token: str = ""
    chat_id: str = ""

class AIModels(BaseModel):
    translate: str = "gemini-2.0-flash"
    summarize: str = "gemini-2.0-flash"
    readme: str = "gemini-2.0-flash"

class AIConfig(BaseModel):
    provider: str = "gemini"
    api_key: str = ""
    models: AIModels = AIModels()

class GitHubConfig(BaseModel):
    webhook_secret: str = ""

class ServerConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8585

class ChaparConfig(BaseModel):
    telegram: TelegramConfig = TelegramConfig()
    ai: AIConfig = AIConfig()
    github: GitHubConfig = GitHubConfig()
    server: ServerConfig = ServerConfig()