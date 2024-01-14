from src.agents.Agent import Agent


class StoryAgent(Agent):
    def __init__(self, world_agent_summary: str, character_agent_summary: str, context_ending_summary: str,
                 detail_multiplier=1):
        super().__init__(
            name="StoryAgent",
            role="""         
                You specialize in creating events for books.
                
                It is your job to create a huge number of events that start from the beginning of the book and lead
                up to a final event that you will be provided with. You should take into account the users
                already designed world, his already created characters and the final event that he thought of.
        
                Put the word "Chapter" in front of every chapter! Make a bullet point starting with "-" for every event!
                
                Think of as many events as possible along the way.
                Generate at least 50 events.
                """,
            opening_statement_instructions="",
            model="gpt-3.5-turbo-1106"
        )
        self.take_user_input(world_agent_summary)
        self.take_user_input(character_agent_summary)
        self.take_user_input(context_ending_summary)
        self.detail_multiplier = detail_multiplier
        self.story = ""
        self.events = []

    def generate_events(self):
        print("~ event generation")
        self.story = self.generate_response()
        self.split_events()
        print("~ number of generated chapters = " + str(len(self.events)))
        print("~ chapters: " + str(self.events))
        return self.events

    def split_events(self):
        self.events = str(self.story).split("Chapter")
        if len(self.events[0]) < 20:
            self.events = self.events[1:]
        for i in range(len(self.events) - 1):
            self.events[i] = "Chapter" + self.events[i]
