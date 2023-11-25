from openai import OpenAI
from agents.CentralAgent import CentralAgent

# OpenAI Client
client = OpenAI()

# Agents
central_agent = CentralAgent()

# Main
active_agent = central_agent

active_agent.conduct_conversation()
