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
'''
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
event_agent = EventAgent(ph.world_information, ph.character_information)
event_agent.start_conversation()
final_event_information = event_agent.get_final_event()
ConsoleHelpers.create_space()
'''
# StoryAgent
story_agent = StoryAgent(ph.world_information, ph.character_information, ph.final_event_information)
events = story_agent.generate_events()

# AuthorAgent
author_agent = AuthorAgent(ph.central_information, ph.world_information, ph.character_information, events)
author_agent.generate_book()

for chapter in author_agent.chapters:
    print(chapter.chapter)


# # streamlit
# # assistance api
#
#
# event_agent = EventAgent(world_agent.conversation_summary, character_agent.conversation_summary)
# event_agent = EventAgent(world_information, character_information)
# ConsoleHelpers.print_waiting_for_generation_message()
# event_information = event_agent.start_conversation()
# event_agent.agent_print(event_information)
#
# story_agent = StoryAgent(world_agent.conversation_summary, character_agent.conversation_summary, event_agent.final_event)
# generate_story_events = story_agent.generate_events()
# story_agent.agent_print(generate_story_events)
'''
story_agent = StoryAgent(world_information, character_information, final_event_information, 1)
story = story_agent.generate_events()
new_events_list = story_agent.create_events_between()
for event in new_events_list:

    print(f"EVENT:{event}")
'''

'''
structure_agent = StructureAgent(story_information)
structure_information = structure_agent.book_structure
structure_agent.write_chapters_into_list(structure_information)
'''
#
# author_agent = AuthorAgent()
# for chapter in structure_agent.list:
#     print(author_agent.write_chapter(str(chapter)))
