from openai import OpenAI

from src.agents.Agent import Agent


class EventAgent(Agent):
    def __init__(self, world_agent_summary: str, character_agent_summary: str):
        super().__init__(
            name="EventAgent",
            role="""
                You are an experienced book author who is particularly good at developing exciting and unexpected plots 
                for the endings of a book. As input, you will be given an already designed world and all the characters 
                for the book. 
                
                Your task is to create the final event that the books story leads to and where the final plot is
                revealed. You are not allowed to go further into detail or try to write actual pages. It is your job
                to great a general final event that harmonises perfectly with the given world and characters.
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.context.append({"role": "user", "content": world_agent_summary})
        self.context.append({"role": "user", "content": character_agent_summary})

    def generate_end_of_story(self):
        return self.take_input_and_generate_response(
            "Create the ending event of my book and describe it in less than six sentences!"
        )
