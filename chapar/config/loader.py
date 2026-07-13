"""Load and merge configuration from multiple sources."""

from pathlib import Path
import yaml
from chapar.config.schema import ChaparConfig


def load_config(project_path: str = ".") -> ChaparConfig:
    """Load configuration from a project's chapar.yaml file."""
    config_file = Path(project_path) / "chapar.yaml"

    if not config_file.exists():
        return ChaparConfig()  # Return default config if file doesn't exist
    
    raw_text = config_file.read_text()
    data = yaml.safe_load(raw_text)

    return ChaparConfig(**data)
