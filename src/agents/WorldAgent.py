from src.agents.Agent import Agent
from src.utils import ConsoleHelpers, InputChecker


class WorldAgent(Agent):
    def __init__(self, central_agent_summary: str):
        super().__init__(
            name="WorldAgent",
            role="""
                You specialize in designing worlds for books.
                
                It is your job to design a captivating world that builds onto the general idea that the user has
                for their book.
                
                After you have developed a world for the users book, propose it to the user and let them give
                you their opinions on thw world that you have created. Engage in a back and forth discussion
                with the user where you integrate the users feedback into the new worlds you create.
                If you have proposed a world to the user and they ask you to integrate something into the world.
                Integrate the given thing into your created world and propose the adjusted version.
        
                The world should not only be captivating but also described in a way that the user can feel
                the world as they read its description.
                """,
            opening_statement_instructions=("Greet me and explain to me in about three sentences, what your role is. "
                                            "Also tell me that you are going to propose a first idea to the user and "
                                            "tell the user that they can request changes as they like."),
            model="gpt-4-1106-preview"
        )

        self.take_user_input(central_agent_summary)

    def start_conversation(self):
        ConsoleHelpers.print_command_list()
        self.agent_print(self.opening_statement)
        ConsoleHelpers.press_enter_to_continue()
        self.conduct_conversation()

    def conduct_conversation(self):
        self.agent_print(self.generate_world())

        user_input: str = ConsoleHelpers.get_user_input()

        if InputChecker.should_skip_process(user_input):
            self.end_conversation()
            return

        if InputChecker.should_repeat_process(user_input):
            self.reset_context()
            self.start_conversation()
            return

        self.conduct_conversation()

    def generate_world(self):
        return self.take_input_and_generate_response(("Create a world based on my general idea for the book, "
                                                      "describe it in less than six sentences and propose it to me!"))

    def end_conversation(self) -> None:
        self.summarize_conversation()
        self.agent_print("The following will be the world for your book: \n")
        self.agent_print(self.conversation_summary)
        ConsoleHelpers.press_enter_to_continue()

    def summarize_conversation(self):
        self.conversation_summary: str = self.take_input_and_generate_response(("That is enough for now, I am happy "
                                                                                "with the result. Please describe "
                                                                                "the final idea for the world one "
                                                                                "more time."))
