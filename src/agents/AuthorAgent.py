from src.StandardChatGPT import StandardChatGPT
from src.agents.Agent import Agent
from src.utils.ChapterContainer import ChapterContainer


class AuthorAgent(Agent):
    def __init__(self, central_information, world_information, character_information, chapters_as_event_collections):
        super().__init__(
            name="AuthorAgent",
            role="""
                You are a skilled book writer.
                
                It is your job to write chapters for the book that the user has in mind. The user is going
                to provide you with general information on overarching parameters, characters and the books world.
                Try to build onto that within your chapter.
                The user is also going to give you a few points on events that should happen within the chapter
                you are supposed to write. You dont need to follow that completely rigorously, its more important
                that you develop an interesting, coherent story. You are encouraged to add small events here and there
                and to really flesh out and connect the events that were given to you into engaging detail.
                Furthermore, if the use has already written a chapter prior to yours, he is going to give you a brief
                summary of how it ends. In that case, try to write the chapter so that it smoothly transitions from
                the last chapter, to the one your writing.
                
                Dont write the text to elegantly. It should be generic and appealing to read.
                """,
            opening_statement_instructions="",
            model="gpt-3.5-turbo-1106"
        )
        self.chapter_as_event_collections = chapters_as_event_collections
        self.chapters: list[ChapterContainer] = []

        self.chat_gpt = StandardChatGPT()

        self.take_user_input(central_information)
        self.take_user_input(world_information)
        self.take_user_input(character_information)

    def generate_book(self):
        print("~ book generation")
        for index, event_collection in enumerate(self.chapter_as_event_collections):
            if index == 0:
                print("~ chapter 1 generation")
                self.generate_chapter(event_collection)
            else:
                print("~ chapter " + str(index + 1) + " generation")
                self.generate_chapter(event_collection, self.chapters[index - 1].chapter_ending_summary)

    def generate_chapter(self, events_descriptions, prior_chapter_ending_summary=""):
        lines_within_events = events_descriptions.split('\n')

        events = [line for line in lines_within_events if '-' in line]

        chapter: str = ""

        last_event = ""

        for index, event in enumerate(events):
            if index == 0:
                self.take_user_input("This is going to be a new chapter, please start the chapter with its name.")
                if prior_chapter_ending_summary != "":
                    chapter += self.generate_transition(prior_chapter_ending_summary, event)
            else:
                chapter += self.generate_transition(events[index - 1], event)

            chapter += self.generate_event_text(event)

            last_event = event

        self.chapters.append(ChapterContainer(chapter, last_event))

        self.revert_context()

    def generate_transition(self, last_event, next_event):
        self.take_user_input("The following is a summary of the last event that occurred.")
        self.take_user_input(last_event)
        self.take_user_input("The following is a summary of the next event that will follow.")
        self.take_user_input(next_event)

        instructions = """
        Write a big part for the book where the story calmly transitions from the last event
        to the next one. You can introduce resting periods, on-the-side-conversations and even
        let the characters complete small side quests.
        """

        transition = self.take_input_and_generate_response(instructions)

        self.revert_context()

        return transition

    def generate_event_text(self, event_description) -> str:
        self.take_user_input("The following is an event that happens within the chapter.")
        self.take_user_input(event_description)

        instructions = """
        Please write out the event in absolute detail, add things to it and make it as long as possible.
        """

        event_text = self.take_input_and_generate_response(instructions)

        self.revert_context()

        return event_text

    def revert_context(self):
        self.context = self.context[:4]
