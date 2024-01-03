from src.StandardChatGPT import StandardChatGPT
from src.agents.Agent import Agent
from src.utils import ConsoleHelpers, InputChecker


class CentralAgent(Agent):
    def __init__(self):
        super().__init__(
            name="CentralAgent",
            role="""
                You are a skilled book writer who's knowledge specializes in creating a general idea for a book.
                It's your job to help the user develop a general idea for what his first book could look like in a
                professional back and forth discussion, without going further into detail.
                
                Parameters that the user should think about could for example be the book's genre, setting, location,
                number of main characters (not their details), approximate length, target audience, the message it shall 
                convey etc.
                """,
            opening_statement_instructions="""
                Greet me and explain to me in about three sentences, what your role is. Ask me afterwards, if I already 
                have some ideas for my book.
                """
        )

    def start_conversation(self):
        ConsoleHelpers.print_command_list()
        self.agent_print(self.opening_statement)
        self.conduct_conversation()

    def conduct_conversation(self):
        user_input = input()
        self.take_user_input(user_input)

        if self.has_user_given_enough_information() and not self.is_user_asking_something(user_input):
            self.end_conversation()
        elif InputChecker.should_skip_process(user_input):
            self.end_conversation()
        elif InputChecker.should_repeat_process(user_input):
            self.reset_context()
            self.start_conversation()
        else:
            self.agent_print(self.generate_response())
            self.conduct_conversation()

    def end_conversation(self) -> None:
        self.summarize_conversation()

    def summarize_conversation(self):
        self.take_user_input(("Thanks for your help. The back and fourth is now done. "
                              "For all the points I have not given you information on, generate examples and use the "
                              "first one of every point for my book."))

        self.conversation_summary: str = self.take_input_and_generate_response(("Summarize what I have envisioned for "
                                                                                "my book. Only cover the information "
                                                                                "that you are supposed to ascertain "
                                                                                "according to your role."))

    def is_user_asking_something(self, user_input) -> bool:
        context_copy: list[dict[str, str]] = self.get_context_copy()

        chat_gpt = StandardChatGPT(context_copy)
        response: str = chat_gpt.generate_response(
            ("Have I asked you something in my last message?"
             "Respond with \"1\" if yes. Respond with \"0\" if not.")
        )

        return response == "1"

    def has_user_given_enough_information(self) -> bool:
        context_copy: list[dict[str, str]] = self.get_context_copy()

        chat_gpt = StandardChatGPT(context_copy)
        response: str = chat_gpt.generate_response(
            ("Have I given you Information on all of the points you are supposed to collect from me"
             "for my book? Respond with \"1\" if so. Respond with \"0\" if not.")
        )

        return response == "1"
