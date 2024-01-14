from src.agents.Agent import Agent


class StoryAgent(Agent):
    def __init__(self, world_agent_summary: str, character_agent_summary: str, context_ending_summary: str,
                 detail_multiplier = 1):
        super().__init__(
            name="StoryAgent",
            role="""         
                You specialize in creating events for books.
                
                It is your job to create a huge number of events that start from the beginning of the book and lead
                up to a final event that you will be provided with. You should take into account the users
                already designed world, his already created characters and the final event that he thought of.
        
                Generate at least 50 events that you put into bullet points and structure them into different chapters.
                Create at least 7 events per chapter.
                """,
            opening_statement_instructions=""
        )
        self.take_user_input(world_agent_summary)
        self.take_user_input(character_agent_summary)
        self.take_user_input(context_ending_summary)
        self.detail_multiplier = detail_multiplier
        self.story = ""
        self.events = []

    def generate_events(self):
        self.story = self.generate_response()
        self.split_events()
        return self.events

    def more_details(self):
        while self.detail_multiplier > 0:
            self.story = self.take_input_and_generate_response("""
            Take all of the bullet points you have created for the events. Add new events in-between and make them fit
            in. Write a ";" at the end of every event you generate. Please tell me the entirety of the events that now
            exist. The ";" at the end of every event is very important. Check again if it is there.
            """)
            self.detail_multiplier -= 1

    def split_events(self):
        self.events = str(self.story).split("Chapter")
        self.events = self.events[1:]
        for i in range(len(self.events) - 1):
            self.events[i] = "Chapter" + self.events[i]
            self.events[i] = self.events[i][:-7]



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
            new_events_list.append(self.events[i])
            new_events_list.append(new_event)
            print(f"old event{self.events[i]}")
            print(f"NEW EVENT{new_event}")

        print(f"old event{self.events[-1]}")
        new_events_list.append(self.events[-1])
        self.events = new_events_list
        return new_events_list
