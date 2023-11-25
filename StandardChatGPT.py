from openai import OpenAI


class StandardChatGPT:
    def __init__(self):
        self.client = OpenAI()
        self.name = "ChatGPT"
        self.context = []

    def generate_response(self, user_request):
        self.context.append({"role": "user", "content": user_request})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response: str = completion.choices[0].message.content

        self.context.append({"role": "assistant", "content": response})

        return f"[{self.name}]: {response}"
