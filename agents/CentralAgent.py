from openai import OpenAI

class CentralAgent():
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
