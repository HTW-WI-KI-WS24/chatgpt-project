from src.agents.Agent import Agent
from src.utils import ConsoleHelpers


class WorldAgent(Agent):
    def __init__(self, central_agent_summary: str):
        super().__init__(
            name="WorldAgent",
            role="""
                You are a skilled book author who is particularly good at designing worlds for books. 
                The worlds you design are well thought out. You receive input that contains general information about 
                a book, that is supposed to be written. You use this information to design a fitting world. You have 
                freedom in designing the world, as long as it is essentially related to the input. The world should not 
                only be described superficially by you, but in great detail. Important: You dont make the story of the 
                book. You just build the empty world, where the book can play in. Another agent builds the story and the 
                character, so dont create any information about the protagonist and other main characters. Focus 
                primarily on the description of the world and how the various elements should affect the reader. The 
                reader should be given a feeling. 
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )

        self.take_user_input(central_agent_summary)

    def start_conversation(self):
        ConsoleHelpers.print_command_list()
        self.agent_print(self.opening_statement)
        self.conduct_conversation()

    def generate_world(self):
        return self.take_input_and_generate_response(("Create a world based on my general idea for the book and "
                                                      "describe it in less than six sentences!"))
