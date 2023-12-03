from src.agents.CentralAgent import CentralAgent
from src.agents.CharacterAgent import CharacterAgent
from src.agents.EventAgent import EventAgent
from src.agents.WorldAgent import WorldAgent
from src.utils import ConsoleHelpers


# Greet and introduce user
ConsoleHelpers.print_line()
print(
    f"""
[BookGPT]: Welcome!
This software supports you in writing any book you can imagine.
You will be lead through various processes by a number of
professional book-writers, aiming to make writing your own
book as simple as possible for you.

    """
)
input(f"\nPress {ConsoleHelpers.make_cursive("Enter")} to continue...")
ConsoleHelpers.create_space()

# Start conversation with CentralAgent
central_agent = CentralAgent()
central_agent.conduct_conversation()
ConsoleHelpers.create_space()

# Start conversation with WorldAgent
world_agent = WorldAgent(central_agent.conversation_summary)
print(ConsoleHelpers.convert_to_block_text((world_agent.attach_name(world_agent.generate_opening_statement()))))
input(f"\nPress {ConsoleHelpers.make_cursive("Enter")} to continue...")
print(ConsoleHelpers.make_cursive("generating...\n"))
world_information = world_agent.generate_world()
print(ConsoleHelpers.convert_to_block_text(world_agent.attach_name(world_information)))
input(f"\nPress {ConsoleHelpers.make_cursive("Enter")} to continue...")
print(ConsoleHelpers.make_cursive("generating...\n"))
ConsoleHelpers.create_space()

# Start conversation with CharacterAgent
character_agent = CharacterAgent(central_agent.conversation_summary, world_information)
print(ConsoleHelpers.convert_to_block_text((character_agent.attach_name(character_agent.generate_opening_statement()))))
input(f"\nPress {ConsoleHelpers.make_cursive("Enter")} to continue...")
print(ConsoleHelpers.make_cursive("generating...\n"))
character_information = character_agent.generate_response()
print(ConsoleHelpers.convert_to_block_text(character_information))
input(f"\nPress {ConsoleHelpers.make_cursive("Enter")} to continue...")
print(ConsoleHelpers.make_cursive("generating...\n"))
ConsoleHelpers.create_space()

# Start conversation with EventAgent
event_agent = EventAgent(world_information, character_information)
print(ConsoleHelpers.convert_to_block_text((event_agent.attach_name(event_agent.generate_opening_statement()))))
input(f"\nPress {ConsoleHelpers.make_cursive("Enter")} to continue...")
print(ConsoleHelpers.make_cursive("generating...\n"))
event_information = event_agent.generate_end_of_story()
print(ConsoleHelpers.convert_to_block_text(event_information))

# I want to write an action book with that plays in london 1930. I want to have 3 main characters and my book to be targeted at young adults. I also want my book to be rather short.
