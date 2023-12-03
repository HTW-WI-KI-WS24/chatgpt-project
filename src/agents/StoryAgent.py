from src.agents.Agent import Agent


class StoryAgent(Agent):
    def __init__(
            self,
            world_agent_summary: str,
            character_agent_summary: str,
            context_ending_summary: str
    ):
        super().__init__(
            name="StoryAgent",
            role="""
                As an accomplished book author with a knack for crafting compelling and unpredictable plots, 
                you're tasked with developing events that seamlessly fit into an intricately designed world. 
                The story already features a diverse set of characters and has a predefined ending. Your 
                challenge is to create events that not only align with the given world, characters, and ending 
                but also bring a unique and captivating twist. Craft events that surprise the reader, avoiding 
                clichés and ensuring the narrative flows organically. Your goal is to deliver a storyline that 
                keeps the audience engaged from start to finish.
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.context.append({"role": "user", "content": world_agent_summary})
        self.context.append({"role": "user", "content": character_agent_summary})
        self.context.append({"role": "user", "content": context_ending_summary})

    def generate_events(self):
        return self.generate_response()
