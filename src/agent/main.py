import os
from dotenv import load_dotenv

from src.agent.agent import Agent
from src.emotion.emotion import detect_emotion  
from src.utils.config import Config  lets 
from src.utils.logging import logger

# Load environment variables
load_dotenv()

def main():
    # 1. Load Configuration
    config = Config() 

    # 2. Initialize Logging
    logger.info("leila is coming.")

    # 3. Initialize the Agent
    agent = Agent(config=config)

    # 4. Main Interaction Loop
    print("Leila: Hello! How can I help you today?")
    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ("exit", "quit"):
                print(" Leila: Goodbye! Remember, you are stronger than your fears.")
                break

            # --- 5. Emotion Detection ---
            emotion, confidence = detect_emotion(user_input)
            logger.debug(f"Detected emotion: {emotion} (confidence: {confidence:.2f})")

            # --- 6. Agent Processing ---
            response = agent.process_input(user_input, emotion, confidence)

            # --- 7. Output Response ---
            print(f"🤖 FearlessBot: {response}")

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            print("🤖 FearlessBot: I'm sorry, I encountered an error. Please try again.")

if __name__ == "__main__":
    main()