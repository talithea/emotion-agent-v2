"""
Main entry point for Leila chatbot.
Runs the interactive conversation loop.
"""

import os
from dotenv import load_dotenv

from src.agent.agent import Agent
from src.utils.config import Config


def main():
    """Run the main chatbot loop."""
    # Load environment variables
    load_dotenv()

    # 1. Load Configuration
    try:
        config = Config()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        return

    print(f"✓ Configuration loaded: {config}")

    # 2. Initialize the Agent
    try:
        agent = Agent(config=config)
        print("✓ Agent initialized")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return

    # 3. Main Interaction Loop
    print("\n🤖 Leila: Hello! I'm Leila. How can I help you today?")
    print("(Type 'exit' or 'quit' to end the conversation)\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ("exit", "quit"):
                print("\n🤖 Leila: Goodbye! Remember, you are stronger than your fears. 💪")
                break

            if not user_input:
                continue

            # --- Process Input ---
            response = agent.process_input(user_input)

            # --- Output Response ---
            print(f"🤖 Leila: {response}\n")

        except KeyboardInterrupt:
            print("\n\n👋 Conversation interrupted. Take care!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()