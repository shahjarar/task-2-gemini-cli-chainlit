import os
from agents import Agent
from tools import read_user_profile, update_user_profile
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def create_agent():
    """Creates and configures the agent."""

    agent = Agent(
        model="litellm/gemini/gemini-2.0-flash",
        api_key=GEMINI_API_KEY,
        tools=[read_user_profile, update_user_profile],
        instructions="Greet users by name if known. Detect when users share personal info and save it using tools.",
    )
    return agent
