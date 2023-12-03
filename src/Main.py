from src.agents.CentralAgent import CentralAgent
from src.agents.CharacterAgent import CharacterAgent
from src.agents.EventAgent import EventAgent
from src.agents.WorldAgent import WorldAgent
from src.utils import ConsoleHelpers

central_agent = CentralAgent()
central_agent.conduct_conversation()

world_agent = WorldAgent(central_agent.conversation_summary)
world_information = world_agent.generate_world()
print(ConsoleHelpers.convert_to_block_text(world_information))

character_agent = CharacterAgent(central_agent.conversation_summary, world_information)
character_information = character_agent.generate_response()
print(ConsoleHelpers.convert_to_block_text(character_information))

event_agent = EventAgent(world_information, character_information)
print(ConsoleHelpers.convert_to_block_text(event_agent.generate_end_of_story()))
