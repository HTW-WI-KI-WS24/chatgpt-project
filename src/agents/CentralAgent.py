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

    def conduct_conversation(self):
        ConsoleHelpers.print_command_list()
        print(self.attach_name_and_convert_to_block_text(self.opening_statement) + "\n")

        while True:
            user_input = input()
            self.take_user_input(user_input)

            #if self.has_user_asked_to_end_conversation() or self.has_user_given_enough_information():
            #    self.summarize_conversation()
            #    break
            if InputChecker.should_skip_process(user_input):
                self.summarize_conversation()
                break
            elif InputChecker.should_repeat_process(user_input):
                self.reset_context()
                self.conduct_conversation()
                break
            else:
                response: str = self.take_input_and_generate_response(user_input)
                print("\n" + self.attach_name_and_convert_to_block_text(response) + "\n")

        return

    def summarize_conversation(self):
        self.take_user_input(
            """
            Thanks for your help. The back and fourth is now done.
            For all the points I have not given you information on, generate examples and use the first one of every
            point for my book.
            """
        )
        self.conversation_summary: str = self.take_input_and_generate_response(
            """
            Summarize what I have envisioned for my book. Only cover the information that you are supposed to ascertain
            according to your role.
            """
        )

        print("\n" + ConsoleHelpers.convert_to_block_text(self.attach_name(self.conversation_summary)))
        ConsoleHelpers.press_enter_to_continue()

    def has_user_given_enough_information(self):
        context_copy: list[dict[str, str]] = self.get_context_copy()
        context_copy.append(
            {
                "role": "user",
                "content": ("If I have given you enough information on the points you are supposed to discuss with me."
                            "Respond with \"1\". If not: Respond with \"0\"")
            }
        )
        completion = self.client.chat.completions.create(model=self.model, messages=context_copy)
        response: str = completion.choices[0].message.content

        has_user_given_enough_information: bool = False
        if response == "1":
            has_user_given_enough_information = True
        return has_user_given_enough_information
