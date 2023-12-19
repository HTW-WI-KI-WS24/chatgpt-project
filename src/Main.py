import streamlit as st

from src import BookGPT
from src.agents.CentralAgent import CentralAgent
from src.agents.CharacterAgent import CharacterAgent
from src.agents.EventAgent import EventAgent
from src.agents.WorldAgent import WorldAgent
from src.utils import ConsoleHelpers

# Greet and introduce user
ConsoleHelpers.print_line()
print(ConsoleHelpers.convert_to_block_text(BookGPT.welcome_message))
ConsoleHelpers.press_enter_to_continue()
ConsoleHelpers.create_space()

# Start conversation with CentralAgent
central_agent = CentralAgent()
central_agent.conduct_conversation()
ConsoleHelpers.create_space()

# Start conversation with WorldAgent
world_agent = WorldAgent(central_agent.conversation_summary)
print(world_agent.attach_name_and_convert_to_block_text(world_agent.opening_statement))
ConsoleHelpers.press_enter_to_continue()
print(BookGPT.waiting_for_generation_message)
world_information = world_agent.generate_world()
print(ConsoleHelpers.convert_to_block_text(world_agent.attach_name(world_information)))
ConsoleHelpers.press_enter_to_continue()
print(BookGPT.waiting_for_generation_message)
ConsoleHelpers.create_space()

# Start conversation with CharacterAgent
character_agent = CharacterAgent(central_agent.conversation_summary, world_information)
print(character_agent.attach_name_and_convert_to_block_text(character_agent.opening_statement))
ConsoleHelpers.press_enter_to_continue()
print(BookGPT.waiting_for_generation_message)
character_information = character_agent.generate_response()
print(ConsoleHelpers.convert_to_block_text(character_information))
ConsoleHelpers.press_enter_to_continue()
print(BookGPT.waiting_for_generation_message)
ConsoleHelpers.create_space()

# Start conversation with EventAgent
event_agent = EventAgent(world_information, character_information)
print(event_agent.attach_name_and_convert_to_block_text(event_agent.opening_statement))
ConsoleHelpers.press_enter_to_continue()
print(BookGPT.waiting_for_generation_message)
event_information = event_agent.generate_end_of_story()
print(ConsoleHelpers.convert_to_block_text(event_information))

# I want to write an action book with that plays in london 1930. I want to have 3 main characters and my book to be targeted at young adults. I also want my book to be rather short.
