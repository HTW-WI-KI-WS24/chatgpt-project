# import streamlit as st

import BookGPT
from agents.CentralAgent import CentralAgent
from agents.CharacterAgent import CharacterAgent
from agents.EventAgent import EventAgent
from agents.WorldAgent import WorldAgent
from agents.StoryAgent import StoryAgent
from agents.StructureAgent import StructureAgent
from agents.AuthorAgent import AuthorAgent
from src.utils.PromptHelpers import world_information, character_information
from utils import ConsoleHelpers

# Greet and introduce user
# ConsoleHelpers.print_line()
# BookGPT.introduce_application()
# ConsoleHelpers.create_space()

# Start conversation with CentralAgent
# central_agent = CentralAgent()
# central_agent.start_conversation()
# ConsoleHelpers.create_space()
#
# # Start conversation with WorldAgent
# world_agent = WorldAgent(central_agent.conversation_summary)
# world_agent.start_conversation()
# ConsoleHelpers.create_space()
#
# # Start conversation with CharacterAgent
# character_agent = CharacterAgent(central_agent.conversation_summary, world_agent.conversation_summary)
# character_agent.start_conversation()
# ConsoleHelpers.create_space()
#
# # Start conversation with EventAgent
# # event_agent = EventAgent(world_agent.conversation_summary, character_agent.conversation_summary)
# # event_agent.agent_print(event_agent.opening_statement)
# # ConsoleHelpers.press_enter_to_continue()
# # event_information = event_agent.generate_end_of_story()
# # event_agent.agent_print(event_information)
#
# # I want to write an action book with that plays in london 1930. I want to have 3 main characters and my book to be
# # targeted at young adults. I also want my book to be rather short.
#
# # streamlit
# # assistance api
#
#
# event_agent = EventAgent(world_information, character_information)
# ConsoleHelpers.print_waiting_for_generation_message()
# event_information = event_agent.start_conversation()
# # event_agent.agent_print(event_information)
#
# story_agent = StoryAgent(world_agent.conversation_summary, character_agent.conversation_summary, event_agent.final_event)
# generate_story_events = story_agent.generate_events()
# story_agent.agent_print(generate_story_events)

# structure_agent = StructureAgent(generate_story_events)
generate_story_events = """
Start of the story: - Ariella, a skilled archer and member of the Eldorian royal guard, 
becomes plagued by recurring nightmares that seem to foretell the destruction of their realm. - Determined 
to uncover the truth behind these visions, Ariella seeks the guidance of a renowned seer, who reveals 
the existence of an ancient curse that has befallen Eldoria. - Ariella sets out on a perilous journey 
to find a way to break the curse and save her people, even if it means venturing into the unknown. Events: 
1. Ariella's Quest Begins: - Ariella, armed with her trusty bow and quiver, sets out on her quest to 
seek answers, leaving behind her comfortable life in the royal palace. - She faces treacherous terrains, 
encounters mythical creatures, and battles her inner fears as she navigates through the enchanted forests 
and treacherous mountains of Eldoria. 2. Unexpected Alliance: - While navigating through a dense forest, 
Ariella encounters Doran, a rogue thief with a quick wit and agility unmatched by anyone she's ever met. 
- Initially at odds, the duo reluctantly forms an alliance when they realize they share a common goal 
- to break the curse that plagues Eldoria. - Together, they face numerous challenges, relying on each 
other's unique skills to overcome obstacles and enemies standing in their way. 3. Secret of the Krater 
von Azul: - Following a trail of mythical legends, Ariella and Doran uncover clues that lead them to 
the Krater von Azul, a dormant volcano rumored to hold the key to breaking the curse. - In their journey 
to the summit, they encounter Lysander, a mysterious and enigmatic sorcerer who has been tracking the 
curse for his own reasons. - Lysander joins their quest, bringing his vast knowledge of arcane magic 
and mystic artifacts, adding a new layer of complexity to the group dynamics. 4. Unveiling the Hidden 
Chamber: - In a dramatic turn of events, their quest leads them deep beneath the Krater von Azul, where 
they discover a hidden chamber pulsing with dark energy. - The chamber is adorned with ancient runes 
and guarded by powerful enchantments, testing their unity and resolve. - Ariella, using her exceptional 
archery skills, must hit a series of precise targets to deactivate the magical defenses and unlock the 
chamber's secrets. 5. The Otherworldly Artifact: - Inside the chamber, Ariella, Doran, and Lysander find 
an otherworldly artifact glowing with malevolent energy. - They realize that this artifact is the source 
of the curse that plagues Eldoria and must decide how to handle its power. - Tensions rise as each character's 
motivation and desires come to light, testing the strength of their newfound alliance. 6. Shattering 
the Artifact: - In a moment of self-sacrifice, Ariella takes a bold leap and shatters the artifact with 
her arrows, releasing a burst of magical light that illuminates the chamber. - The burst of light purges 
the curse from Eldoria, restoring balance and bringing an end to the suffering that plagued the realm 
for centuries. - The group's combined efforts and unity prove to be the key to their success, and in 
the aftermath, they forge a bond that will forever tie them together. The events leading up to the final 
confrontation between Ariella, Doran, and Lysander with the otherworldly artifact will provide the necessary 
complexity and length for the book. These events will test their strengths and weaknesses, explore their 
individual and collective motivations, and ultimately shape their characters as they work together to 
save Eldoria. 
"""

structure_agent = StructureAgent(generate_story_events)
structure_information = structure_agent.book_structure
structure_agent.write_chapters_into_list(structure_information)

author_agent = AuthorAgent(structure_agent.list)
# author_agent.write_chapter_into_textfile("test\n")
for chapter in structure_agent.list:
    print(author_agent.write_chapter(str(chapter)) + "\n")
