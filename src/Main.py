# import streamlit as st

import BookGPT
from agents.CentralAgent import CentralAgent
from agents.CharacterAgent import CharacterAgent
from agents.EventAgent import EventAgent
from agents.WorldAgent import WorldAgent
from src.utils.PromptHelpers import world_information
from utils import ConsoleHelpers

# Greet and introduce user
ConsoleHelpers.print_line()
BookGPT.introduce_application()
ConsoleHelpers.create_space()

# Start conversation with CentralAgent
central_agent = CentralAgent()
central_agent.start_conversation()
ConsoleHelpers.create_space()

# Start conversation with WorldAgent
world_agent = WorldAgent(central_agent.conversation_summary)
world_agent.start_conversation()
ConsoleHelpers.create_space()

# Start conversation with CharacterAgent
character_agent = CharacterAgent(central_agent.conversation_summary, world_agent.conversation_summary)
character_agent.agent_print(character_agent.opening_statement)
ConsoleHelpers.press_enter_to_continue()
character_information = character_agent.generate_response()
character_agent.agent_print(character_information)
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.create_space()

# Start conversation with EventAgent
event_agent = EventAgent(world_agent.conversation_summary, character_information)
event_agent.agent_print(event_agent.opening_statement)
ConsoleHelpers.press_enter_to_continue()
event_information = event_agent.generate_end_of_story()
event_agent.agent_print(event_information)

# I want to write an action book with that plays in london 1930. I want to have 3 main characters and my book to be
# targeted at young adults. I also want my book to be rather short.

# streamlit
# assistance api


event_agent = EventAgent(world_information, character_information)
ConsoleHelpers.print_waiting_for_generation_message()
event_information = event_agent.start_conversation()
# event_agent.agent_print(event_information)
