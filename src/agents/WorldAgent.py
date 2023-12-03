from src.agents.Agent import Agent


class WorldAgent(Agent):
    def __init__(
            self,
            central_agent_summary: str
    ):
        super().__init__(
            name="WorldAgent",
            role="""
                You are a skilled book author who is particularly good at designing worlds for books. 
                The worlds you design are well thought out. You receive input that contains data about a book, 
                which is to be written. You use this data to design a corresponding world. You have freedom in designing the world,
                as long as it is essentially related to the input. The world should not only be described superficially by you, 
                but in great detail. Important: You dont make the story of the book. You just build the empty world, where the book can 
                play in. Another agent builds the story and the character, so dont create any Informations about the protagonist and other main characters.
                Focus primarily on the description of the world and how the various elements should affect the reader. The reader should be given a feeling. 
                """,
            opening_statement_instructions="Greet me and explain shortly what your Role is. Max 3 Sentences"
        )
        self.context.append({"role": "user", "content": central_agent_summary})

    def generate_world(self):
        self.generate_response()
