from src.utils import ConsoleHelpers, InputChecker
from src.agents.Agent import Agent


class EventAgent(Agent):
    def __init__(self, world_agent_summary: str, character_agent_summary: str):
        super().__init__(
            name="EventAgent",
            role="""
                You are an experienced book author who is particularly good at developing exciting and unexpected plots for the end of a book. 
                You will be given an already designed world and all the characters for the book as input.
                Your task is to design the final event to which the story of the book leads and in which the final plot is revealed. 
                You are not allowed to go into detail or try to write specific pages. 
                It is your job to create a general final event that harmonises perfectly with the given world and characters. 
                Your output should be short and general. 
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.context.append({"role": "user", "content": world_agent_summary})
        self.context.append({"role": "user", "content": character_agent_summary})
        self.final_event = ""

    def generate_end_of_story(self):
        self.final_event = self.take_input_and_generate_response(
            "Create the ending event of my book and describe it in less than six sentences!"
        )
    
    def start_conversation(self):
        ConsoleHelpers.print_command_list()
        self.agent_print(self.opening_statement)
        self.agent_print("""I have designed the following ending for you. 
                         If you are not satisfied with the ending or would like to make changes, please let me know. 
                         For example, if you want to kill a character, you can do it here completely legally ;)""")
        self.generate_end_of_story()
        self.conduct_conversation()

    def conduct_conversation(self):
        
        self.agent_print(self.final_event)
        user_input = input()
        self.take_user_input(user_input)

        if InputChecker.should_skip_process(user_input):
            self.end_conversation_and_return_event()
        elif InputChecker.should_repeat_process(user_input):
            self.reset_context()
            self.start_conversation()
        else:
            self.final_event = self.generate_response()
            self.conduct_conversation()

    def summarize_conversation(self):

        self.conversation_summary: str = self.take_input_and_generate_response(("""Summarise what I have in mind for my book. 
                                                                                Make sure you include all my wishes in the ending"""))
    
    def end_conversation_and_return_event(self):
        return self.final_event