"""
Emotion detection module for Leila chatbot.
Uses pre-trained transformers to classify emotions from text.
"""

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from typing import Tuple, Dict, List, Any


class EmotionDetector:
    """
    Detects emotions from text using pre-trained models.
    """

    def __init__(self, model_name: str, tokenizer_name: str, device: str = "cpu"):
        """
        Initialize emotion detector.

        Args:
            model_name: Name of pre-trained model on Hugging Face
            tokenizer_name: Name of tokenizer on Hugging Face
            device: "cpu" or "cuda"
        """
        self.device = 0 if device == "cuda" and torch.cuda.is_available() else -1
        
        # Load tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        
        # Create pipeline for inference
        self.pipeline = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )

    def detect(self, text: str) -> Tuple[str, float]:
        """
        Detect the primary emotion from text.

        Args:
            text: Input text to analyze

        Returns:
            Tuple of (emotion_label, confidence_score)
            Example: ("fear", 0.87)
        """
        result = self.pipeline(text, return_all_scores=False)[0]
        return result["label"].lower(), result["score"]

    def detect_all_scores(self, text: str) -> List[Dict[str, Any]]:
        """
        Get scores for all emotion classes.

        Args:
            text: Input text to analyze

        Returns:
            List of dicts with "label" and "score" keys
        """
        return self.pipeline(text, return_all_scores=True)


# Global instance
_detector = None


def init_emotion_detector(model_name: str, tokenizer_name: str, device: str = "cpu") -> None:
    """Initialize global emotion detector."""
    global _detector
    _detector = EmotionDetector(model_name, tokenizer_name, device)


def detect_emotion(text: str) -> Tuple[str, float]:
    """
    Detect emotion from text using global detector.

    Args:
        text: Input text to analyze

    Returns:
        Tuple of (emotion_label, confidence_score)
    """
    if _detector is None:
        raise RuntimeError(
            "Emotion detector not initialized. Call init_emotion_detector() first."
        )
    return _detector.detect(text)


def detect_emotion_all(text: str) -> List[Dict[str, Any]]:
    """Get all emotion scores for text."""
    if _detector is None:
        raise RuntimeError(
            "Emotion detector not initialized. Call init_emotion_detector() first."
        )
    return _detector.detect_all_scores(text)