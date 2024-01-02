# import streamlit as st

from src import BookGPT
from src.agents.CentralAgent import CentralAgent
from src.agents.CharacterAgent import CharacterAgent
from src.agents.EventAgent import EventAgent
from src.agents.WorldAgent import WorldAgent
from src.utils import ConsoleHelpers

# Greet and introduce user
ConsoleHelpers.print_line()
BookGPT.introduce_application()
ConsoleHelpers.create_space()

# Start conversation with CentralAgent
ConsoleHelpers.print_waiting_for_generation_message()
central_agent = CentralAgent()
central_agent.start_conversation()
ConsoleHelpers.create_space()

# Start conversation with WorldAgent
ConsoleHelpers.print_waiting_for_generation_message()
world_agent = WorldAgent(central_agent.conversation_summary)
world_agent.agent_print(world_agent.opening_statement)
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.print_waiting_for_generation_message()
world_information = world_agent.generate_world()
world_agent.agent_print(world_information)
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.create_space()

# Start conversation with CharacterAgent
ConsoleHelpers.print_waiting_for_generation_message()
character_agent = CharacterAgent(central_agent.conversation_summary, world_information)
character_agent.agent_print(character_agent.opening_statement)
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.print_waiting_for_generation_message()
character_information = character_agent.generate_response()
character_agent.agent_print(character_information)
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.create_space()

# Start conversation with EventAgent
ConsoleHelpers.print_waiting_for_generation_message()
event_agent = EventAgent(world_information, character_information)
event_agent.agent_print(event_agent.opening_statement)
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.print_waiting_for_generation_message()
event_information = event_agent.generate_end_of_story()
event_agent.agent_print(event_information)

# I want to write an action book with that plays in london 1930. I want to have 3 main characters and my book to be targeted at young adults. I also want my book to be rather short.

# streamlit
# assistance api
