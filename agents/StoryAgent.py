from openai import OpenAI

import InputChecker
from utils import CustomPrinter


class StoryAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "StoryAgent"
        self.context = [
            {
                "role": "system",
                "content": """As an accomplished book author with a knack for crafting compelling and unpredictable plots, 
                  you're tasked with developing events that seamlessly fit into an intricately designed world. 
                  The story already features a diverse set of characters and has a predefined ending. Your 
                  challenge is to create events that not only align with the given world, characters, and ending 
                  but also bring a unique and captivating twist. Craft events that surprise the reader, avoiding 
                  clichés and ensuring the narrative flows organically. Your goal is to deliver a storyline that 
                  keeps the audience engaged from start to finish."""
            }
        ]
        self.conversation_evaluation = ""

    def generate_opening_statement(self):
        temp_context = self.context.copy()
        temp_context.append(
            {"role": "user", "content": "Greet me and explain shortly what your Role is. Max 3 Sentences"})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=temp_context
        )
        opening_statement = completion.choices[0].message.content
        return f"[{self.name}]: {opening_statement}"

    def generate_events(self, user_request, context_world, context_character, context_ending):
        self.context.append({"role": "user", "content": user_request})
        self.context.append({"role": "user", "content": context_world})
        self.context.append({"role": "user", "content": context_character})
        self.context.append({"role": "user", "content": context_ending})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response: str = completion.choices[0].message.content

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
                CustomPrinter.custom_print(self.generate_events(user_input))

        return
