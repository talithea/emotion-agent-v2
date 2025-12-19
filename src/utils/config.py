"""
Configuration management for Leila chatbot.
Loads and validates environment variables and model settings.
"""

import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelConfig:
    """Configuration for emotion detection models."""
    emotion_model_name: str = "j-hartmann/emotion-english-distilroberta-base"
    emotion_tokenizer_name: str = "j-hartmann/emotion-english-distilroberta-base"
    device: str = "cpu"  # "cpu" or "cuda"


@dataclass
class APIConfig:
    """Configuration for external APIs."""
    gemini_api_key: Optional[str] = None
    gemini_model: str = "gemini-2.0-pro"
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta/"


class Config:
    """
    Main configuration class.
    Loads environment variables and initializes all configs.
    """

    def __init__(self):
        """Initialize configuration by loading environment variables."""
        load_dotenv()

        # API Configuration
        self.api = APIConfig(
            gemini_api_key=os.getenv("API_KEY"),
            gemini_model="gemini-2.0-pro"
        )

        # Model Configuration
        self.model = ModelConfig(
            device="cuda" if self._check_cuda() else "cpu"
        )

        # Validate critical settings
        self._validate()

    def _check_cuda(self) -> bool:
        """Check if CUDA is available."""
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False

    def _validate(self) -> None:
        """Validate that all required configs are set."""
        if not self.api.gemini_api_key:
            raise ValueError(
                "API_KEY environment variable is not set. "
                "Please create a .env file with API_KEY=your_key"
            )

    def __str__(self) -> str:
        """String representation of configuration."""
        return (
            f"Config(\n"
            f"  API: model={self.api.gemini_model}\n"
            f"  Model: device={self.model.device}\n"
            f")"
        )
