from openai import OpenAI

class CentralAgent():
    def __init__(self):
        self.client = OpenAI()
        self.name = "CentralAgent"
        self.context = [
            {"role": "system", "content": "You are a skilled book writer and communicator that helps the user with writing their own book. Your job is to help the user find the genre, location and length of their book in a discussion-like back and forth"}
        ]

    def get_response(self, user_request):
        self.context.append({"role": "user", "content": user_request})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        return completion.choices[0].message.content


    def get_opening_statement(self):
        temp_context = self.context
        temp_context.append({"role": "user", "content": "Please explain to me what your role is."})
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=temp_context
        )
        return completion.choices[0].message.content
