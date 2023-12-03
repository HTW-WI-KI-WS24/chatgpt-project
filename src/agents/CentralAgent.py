from src.agents.Agent import Agent
from src.utils import ConsoleHelpers, InputChecker


class CentralAgent(Agent):
    def __init__(self):
        super().__init__(
            name="CentralAgent",
            role="""
                You are a skilled book writer who's knowledge specializes in creating a general idea for a new book.
                It's your job to help the user develop a general idea for what his first book could look like in a
                professional back and forth discussion, without going further into detail.
                Parameters that the user should think about could for example be the book's genre, setting, location,
                number of main characters, approximate length, target audience, the message it shall convey etc.
                """,
            opening_statement_instructions="""
                Greet me and explain to me in about three sentences, what your role is. Ask me afterwards, if I already 
                have some ideas for my book.
                """
        )

    def conduct_conversation(self):
        ConsoleHelpers.print_command_list()
        print(ConsoleHelpers.convert_to_block_text(self.generate_opening_statement()))
        print()

        while True:
            user_input = input()

            if InputChecker.should_skip_process(user_input):
                self.summarize_conversation()
                break
            elif InputChecker.should_repeat_process(user_input):
                self.context = self.context[:1]  # Clears all the context except the role description.
                self.conduct_conversation()
                break
            else:
                print()
                print(
                    ConsoleHelpers.convert_to_block_text(
                        self.attach_name(
                            self.take_input_and_generate_response(user_input)
                        )
                    )
                )
                print()

        return
