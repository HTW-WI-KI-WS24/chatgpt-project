# import streamlit as st

import BookGPT
from agents.CentralAgent import CentralAgent
from agents.CharacterAgent import CharacterAgent
from agents.EventAgent import EventAgent
from agents.WorldAgent import WorldAgent
from agents.StoryAgent import StoryAgent
from agents.AuthorAgent import AuthorAgent
from utils import ConsoleHelpers
from utils import PromptHelpers as ph

# Greet and introduce user
ConsoleHelpers.print_line()
BookGPT.introduce_application()
ConsoleHelpers.create_space()

# Start conversation with CentralAgent
central_agent = CentralAgent()
central_agent.start_conversation()
central_information = central_agent.conversation_summary
ConsoleHelpers.create_space()

# Start conversation with WorldAgent
world_agent = WorldAgent(central_information)
world_agent.start_conversation()
world_information = world_agent.conversation_summary
ConsoleHelpers.create_space()

# Start conversation with CharacterAgent
character_agent = CharacterAgent(central_information, world_information)
character_agent.start_conversation()
character_information = character_agent.conversation_summary
ConsoleHelpers.create_space()

# Start conversation with EventAgent
event_agent = EventAgent(world_information, character_information)
event_agent.start_conversation()
final_event_information = event_agent.get_final_event()
ConsoleHelpers.create_space()

# StoryAgent
story_agent = StoryAgent(world_information, character_information, final_event_information)
events = story_agent.generate_events()

# AuthorAgent
author_agent = AuthorAgent(central_information, world_information, character_information, events)
author_agent.generate_book()

# Save book to a file
with open('Your-Book.txt', 'w') as file:
    for chapter in author_agent.chapters:
        file.write(chapter.chapter + "\n\n\n\n\n")
