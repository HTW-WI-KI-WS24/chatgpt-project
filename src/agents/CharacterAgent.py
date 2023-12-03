from src.agents.Agent import Agent
from src.utils import InputChecker, ConsoleHelpers


class CharacterAgent(Agent):
    def __init__(
            self,
            central_agent_summary: str,
            world_agent_summary: str
    ):
        super().__init__(
            name="CharacterAgent",
            role="""
                You are a skilled book writer who's knowledge specializes in creating interesting characters with
                deep backstories and varying personalities and looks. It's your job to help the user develop a
                a set of characters for the book he is about to write while taking its already existing ideas like
                setting, theme and so on into consideration. It is important that you only focus on your job
                and don't go further into detail.
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.context.append({"role": "user", "content": central_agent_summary})
        self.context.append({"role": "user", "content": world_agent_summary})

    def generate_characters(self):
        return self.take_input_and_generate_response("Please generate characters based on my general idea and world.")
