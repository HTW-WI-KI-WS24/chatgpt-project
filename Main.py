from openai import OpenAI
from agents.CentralAgent import CentralAgent
from agents.WorldAgent import WorldAgent
from agents.EventAgent import EventAgent

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
event_agent = EventAgent()
# print(world_agent.generate_opening_statement())

kontext = "Buch welches in London 1400 spielt. Düstere Atmosphere. Richtet sich an erwachsene. Genre Thriller"
character = "Samuel ein armer Straßenjunge spielt die Hauptrolle. Auf dem Weg lernt er gefährten kennen"

print(event_agent.generate_end_of_story(world_agent.generate_world(kontext), character))
