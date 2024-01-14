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
                Events in bullet Points
                
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.model = "gpt-3.5-turbo-1106"
        self.context.append({"role": "user", "content": world_agent_summary})
        self.context.append({"role": "user", "content": character_agent_summary})
        self.context.append({"role": "user", "content": context_ending_summary})
        self.detail_multiplier = detail_multiplier
        self.story = ""
        self.events = []

    def generate_events(self):
        self.story = self.generate_response()
        self.more_details()
        self.split_events()
        return self.story

    def more_details(self):
        while self.detail_multiplier > 0:
            self.story = self.take_input_and_generate_response("""
            Take the story you have created and expand it. Add new events and make existing ones even more detailed. 
            Make The output much longer! Write a ";" at the end of every Event you generated. The ";" 
            is very important. Check if it is there 
            """)
            self.detail_multiplier -= 1

    def split_events(self):
        self.events = str(self.story).split(";")

    def create_events_between(self):

        new_events_list = []
        for i in range(len(self.events) - 1):
            self.context.append({"role": "user", "content": self.events[i]})
            self.context.append({"role": "user", "content": self.events[i+1]})
            new_event = self.take_input_and_generate_response("""
               Create an Event between the two given. The new event should have the same structure as the two existing 
                events, but its content should form a bridge between them. 
                The content should therefore take place between the events.
                Make the full event behind a bullet point.
                """)
            new_events_list.append(i)
            new_events_list.append(new_event)
            print(f"NEW EVENT{new_event}")
        return new_events_list


        for x in new_events_list:
            print(str(x) + "\n\n")

        return new_events_list
