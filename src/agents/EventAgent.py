from openai import OpenAI

from src.agents.Agent import Agent


class EventAgent(Agent):
    def __init__(
            self,
            world_agent_summary: str,
            character_agent_summary: str
    ):
        super().__init__(
            name="EventAgent",
            role="""
                You are an experienced book author who is particularly good at developing exciting and unexpected plots 
                for the endings of a book. As input, you will be given an already designed world and all the characters 
                for the book. Your task is to create only the ending of the book. Write the outstanding end of the book. 
                Only the great final. The ending must harmonise perfectly with the world and the characters. The end 
                should not be easily predictable.
                """,
            opening_statement_instructions="Greet me and explain shortly what your Role is. Max 3 Sentences"
        )
        self.context.append({"role": "user", "content": world_agent_summary})
        self.context.append({"role": "user", "content": character_agent_summary})

    def generate_end_of_story(self):
        return self.generate_response()
