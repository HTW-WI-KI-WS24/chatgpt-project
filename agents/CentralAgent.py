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
                
                To start of the conversation, ask the user to give you any general ideas that he already has for his
                book and guide him through the process of finding new ones.
                """
             }
        ]

    def generate_opening_statement(self):
        temp_context = self.context
        temp_context.append({"role": "user", "content": "Please explain to me what your role is."})
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
                break
            elif InputChecker.should_repeat_process(user_input):
                self.context = self.context[:1]  # Clears all the context except the role description.
                self.conduct_conversation()
                break
            else:
                CustomPrinter.custom_print(self.generate_response(user_input))

        return
