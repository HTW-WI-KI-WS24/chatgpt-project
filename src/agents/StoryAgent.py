from src.agents.Agent import Agent


class StoryAgent(Agent):
    def __init__(self, world_agent_summary: str, character_agent_summary: str, context_ending_summary: str,
                 detail_multiplier):
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
                Note that you will be given a finished event/finale/end of the book as input. 
                Invent a start of the story that does not yet point to the end. 
                Then create all the intermediate events that occur up to the end. 
                Remember that it is a book and that there must be a certain complexity and length.
                You generate many significant intermediate events between the start of the book and the end. 
                Proceed in bullet points! Each event created between the beginning and end of the book 
                should be placed behind a key point. 
        
                
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.model = "gpt-3.5-turbo-1106"
        self.context.append({"role": "user", "content": world_agent_summary})
        self.context.append({"role": "user", "content": character_agent_summary})
        self.context.append({"role": "user", "content": context_ending_summary})
        self.detail_multiplier = detail_multiplier
        self.story = ""

    def generate_events(self):
        self.story = self.generate_response()
        self.more_details()
        return self.story

    def more_details(self):
        while self.detail_multiplier > 0:
            self.story = self.take_input_and_generate_response("""
            Take the story you have created and expand it. Add new events and make existing ones even more detailed. 
            Make The output much longer! Write a ";" at the end of every Event you generated.
            """)
            self.detail_multiplier -= 1

    def split_events(self):
        events = str(self.story).split()
    #def create_events_between(self):
