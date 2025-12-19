"""
Main Agent class for Leila chatbot.
Orchestrates emotion detection and response generation.
"""

import requests
import json
from typing import Tuple, List
from src.utils.config import Config
from src.emotion.emotion import init_emotion_detector, detect_emotion


class Agent:
    """
    Main chatbot agent.
    Handles conversation flow, emotion detection, and API calls.
    """

    def __init__(self, config: Config):
        """
        Initialize the agent.

        Args:
            config: Configuration object
        """
        self.config = config
        self.conversation_history: List[Tuple[str, str]] = []

        # Initialize emotion detector
        init_emotion_detector(
            model_name=config.model.emotion_model_name,
            tokenizer_name=config.model.emotion_tokenizer_name,
            device=config.model.device
        )

    def process_input(self, user_input: str, emotion: str = None, confidence: float = None) -> str:
        """
        Process user input and generate response.

        Args:
            user_input: User's message
            emotion: Pre-detected emotion (optional)
            confidence: Emotion confidence (optional)

        Returns:
            Bot's response text
        """
        # Detect emotion if not provided
        if emotion is None or confidence is None:
            emotion, confidence = detect_emotion(user_input)

        # Build emotion-aware prompt
        prompt = self._build_prompt(user_input, emotion, confidence)

        # Get response from Gemini
        response = self._get_gemini_response(prompt)

        # Store in history
        self.conversation_history.append((user_input, response))

        return response

    def _build_prompt(self, user_input: str, emotion: str, confidence: float) -> str:
        """
        Build emotion-aware prompt for Gemini.

        Args:
            user_input: User's message
            emotion: Detected emotion
            confidence: Emotion confidence score

        Returns:
            Formatted prompt for Gemini
        """
        system_context = (
            "You are Leia, a gentle, empathetic AI assistant designed to help users "
            "explore and confront their fears in a safe, supportive environment. "
            "Your goal is to encourage growth and emotional resilience."
        )

        emotion_context = (
            f"The user appears to be experiencing {emotion} "
            f"(confidence: {confidence:.2%}). "
            "Respond with empathy, ask thoughtful questions, and help them understand their feelings."
        )

        return f"{system_context}\n\n{emotion_context}\n\nUser: {user_input}"

    def _get_gemini_response(self, prompt: str) -> str:
        """
        Call Gemini API for response.

        Args:
            prompt: Formatted prompt for Gemini

        Returns:
            Response text from Gemini
        """
        url = (
            f"{self.config.api.gemini_base_url}"
            f"models/{self.config.api.gemini_model}:generateContent"
            f"?key={self.config.api.gemini_api_key}"
        )

        headers = {"Content-Type": "application/json"}

        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}]
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)

            if response.status_code == 200:
                response_json = response.json()
                reply = response_json["candidates"][0]["content"]["parts"][0]["text"]
                return reply
            else:
                return f"Error from Gemini API: {response.status_code} - {response.text}"

        except requests.exceptions.RequestException as e:
            return f"Error connecting to Gemini API: {str(e)}"

    def get_history(self) -> List[Tuple[str, str]]:
        """
        Get conversation history.

        Returns:
            List of (user_input, bot_response) tuples
        """
        return self.conversation_history.copy()

    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history = []
