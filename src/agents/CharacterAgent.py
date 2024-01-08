from src.agents.Agent import Agent
from src.utils import ConsoleHelpers, InputChecker


class CharacterAgent(Agent):
    def __init__(self, central_agent_summary: str, world_agent_summary: str):
        super().__init__(
            name="CharacterAgent",
            role="""
                You specialize in designing interesting characters with
                captivating backstories, varying personalities and looks for books.
                
                It is your job to help the user design set of characters that fit into the existing world and the
                general idea that the user has for their book.
                
                After you have developed a the characters for the users book, propose them to the user in less than 
                six sentences each and let them give you their opinions on the characters that you have created. Engage 
                in a back and forth discussion with the user where you integrate the users feedback into your created
                characters. If you have proposed the characters to the user and they ask you to change something about 
                the them. Make changes as requested and propose the adjusted set of characters to the user in less than
                six sentences each.
                
                The characters should all be different from each other with unique features and backstories.
        
                It is important that you only focus on your job and don't go further into detail about possible events
                that might happen to the characters.
                """,
            opening_statement_instructions=("Greet me and explain to me in about three sentences, what your role is. "
                                            "Also tell me that you are going to propose a first idea for the characters"
                                            "and tell me that I can request changes as I like.")
        )

        self.take_user_input("The following is the general idea for my book:\n" + central_agent_summary)
        self.take_user_input("The following is the world in which my story plays out:\n" + world_agent_summary)

    def start_conversation(self):
        ConsoleHelpers.print_command_list()
        self.agent_print(self.opening_statement)
        ConsoleHelpers.press_enter_to_continue()
        self.conduct_conversation()

    def conduct_conversation(self):
        self.agent_print(self.generate_response())

        user_input: str = ConsoleHelpers.get_user_input()

        if InputChecker.should_skip_process(user_input):
            self.end_conversation()
            return

        if InputChecker.should_repeat_process(user_input):
            self.reset_context()
            self.start_conversation()
            return

        self.take_user_input(user_input)
        self.conduct_conversation()

    def end_conversation(self) -> None:
        self.summarize_conversation()
        self.agent_print("These are going to be the characters for your book:\n")
        self.agent_print(self.conversation_summary)
        ConsoleHelpers.press_enter_to_continue()

    def summarize_conversation(self):
        self.conversation_summary: str = self.take_input_and_generate_response(("That is enough for now, I am happy "
                                                                                "with the result. Please describe "
                                                                                "the final set of characters one more"
                                                                                "time."))
