from openai import OpenAI
from utils import CustomPrinter

import InputChecker


class CentralAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "CentralAgent"
        self.context = [
            {"role": "system", "content":
                """
                You are a skilled book writer who's knowledge specializes in creating a general idea for a new book.
                It's your job to help the user devlop a general idea for what his first book could look like in a
                professional back and forth discussion.
                Parameters that he should think about could for example be the book's genre, setting, location,
                number of main characters, approximate length, target audience, the message it shall convey etc.
                """
             }
        ]
        self.conversation_evaluation = ""

    def generate_opening_statement(self):
        temp_context = self.context.copy()
        temp_context.append({"role": "user", "content": "Greet me and explain to me elaborately what your role is " +
                                                        "and ask me if I already have some ideas for my book."})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=temp_context
        )
        opening_statement = completion.choices[0].message.content

        return f"[{self.name}]: {opening_statement}"

    def generate_response(self, user_request):
        self.context.append({"role": "user", "content": user_request})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response: str = completion.choices[0].message.content

        self.context.append({"role": "assistant", "content": response})

        return f"[{self.name}]: {response}"

    def conduct_conversation(self):
        CustomPrinter.custom_print(self.generate_opening_statement(), True, True)

        while True:
            user_input = input()

            if InputChecker.should_skip_process(user_input):
                self.evaluate_conversation()
                break
            elif InputChecker.should_repeat_process(user_input):
                self.context = self.context[:1]  # Clears all the context except the role description.
                self.conduct_conversation()
                break
            else:
                CustomPrinter.custom_print(self.generate_response(user_input))

        return

    def evaluate_conversation(self):
        self.context.append({"role": "user", "content": "Concisely summarize what I have envisioned for my book."})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        conversation_evaluation: str = completion.choices[0].message.content

        self.conversation_evaluation = conversation_evaluation
        print("\n" + conversation_evaluation)
