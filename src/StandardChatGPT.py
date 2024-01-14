from openai import OpenAI


class StandardChatGPT:
    def __init__(self, context=None):
        self.client = OpenAI()
        self.name = "ChatGPT"
        self.context = context

        if self.context is None:
            self.context = []

    def take_user_input(self, user_input: str) -> None:
        self.context.append({"role": "user", "content": user_input})

    def take_user_input_and_generate_response(self, user_input):
        self.take_user_input(user_input)

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response: str = completion.choices[0].message.content

        self.context.append({"role": "assistant", "content": response})

        return response

    def reset_context(self) -> None:
        self.context = []
