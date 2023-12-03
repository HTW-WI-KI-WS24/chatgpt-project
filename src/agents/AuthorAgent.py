from openai import OpenAI
from src.agents.Agent import Agent


class AuthorAgent(Agent):
    def __init__(
            self,
            structure_agent_summary: str,
            recent_chapters_summary: str
    ):
        super().__init__(
            name="AuthorAgent",
            role="""
                You are a proficient book author specializing in crafting chapters based on a 
                predefined structure. Your creative process involves receiving input that includes the chapter's 
                structure and a summary of the preceding chapter. Your task is to seamlessly integrate these elements 
                into the existing narrative, maintaining a consistent writing style throughout.
                """,
            opening_statement_instructions="Greet me and explain shortly what your Role is. Max 3 Sentences"
        )
        self.context.append({"role": "user", "content": structure_agent_summary})
        self.context.append({"role": "user", "content": recent_chapters_summary})

    def write_chapter(self):
        self.generate_response()
