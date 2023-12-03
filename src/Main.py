from src.agents.CentralAgent import CentralAgent
from src.agents.CharacterAgent import CharacterAgent
from src.agents.EventAgent import EventAgent
from src.agents.WorldAgent import WorldAgent

central_agent = CentralAgent()
central_agent.conduct_conversation()

world_agent = WorldAgent(central_agent.conversation_summary)
world_information = world_agent.generate_world()
print(world_information)

character_agent = CharacterAgent(central_agent.conversation_summary, world_information)
character_information = character_agent.generate_response()

event_agent = EventAgent(world_information, character_information)
print(event_agent.generate_end_of_story())
