from openai import OpenAI
from agents.CentralAgent import CentralAgent
from agents.WorldAgent import WorldAgent

# OpenAI Client
client = OpenAI()

# Agents
central_agent = CentralAgent()
'''
# Main
active_agent = central_agent

active_agent.conduct_conversation()
'''
world_agent = WorldAgent()
#print(world_agent.generate_opening_statement())

kontext = "Buch welches in London 1400 spielt. Düstere Atmosphere. Richtet sich an erwachsene. Genre Thriller"
print(world_agent.generate_world(kontext))