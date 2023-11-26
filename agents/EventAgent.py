from openai import OpenAI


class EventAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "EventAgent"
        self.context = [
            {"role": "system", "content":
                """
                You are an experienced book author who is particularly good at developing exciting and unexpected plots for the endings of a book.
                As input, you will be given an already designed world and all the characters for the book. Your task is to create only the ending of the book. 
                Write the outstanding end of the book. Only the great final. The ending must harmonise perfectly with the world and the characters. 
                The end should not be an easy predictable on.
                """
             }
        ]

    def generate_opening_statement(self):
        temp_context = self.context.copy()
        temp_context.append({"role": "user", "content": "Greet me and explain shortly what your Role is. Max 3 Sentences"})
        completion = self.client.chat.completions.create(
            model= "gpt-3.5-turbo",
            messages= temp_context
        )
        opening_statement = completion.choices[0].message.content
        return f"[{self.name}]: {opening_statement}"

    def generate_end_of_story(self, world, character):
        self.context.append({"role": "user", "content": world})
        self.context.append({"role": "user", "content": character})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )

        response: str = completion.choices[0].message.content

        return f"[{self.name}]: {response}"