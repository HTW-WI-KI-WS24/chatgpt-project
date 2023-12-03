from openai import OpenAI


class AuthorAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "AuthorAgent"
        self.context = [
            {
                "role": "system",
                "content": """You are a proficient book author specializing in crafting chapters based on a 
                predefined structure. Your creative process involves receiving input that includes the chapter's 
                structure and a summary of the preceding chapter. Your task is to seamlessly integrate these elements 
                into the existing narrative, maintaining a consistent writing style throughout."""
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

    def generate_events(self, user_request, context_structure, context_summary):
        self.context.append({"role": "user", "content": user_request})
        self.context.append({"role": "user", "content": context_structure})
        self.context.append({"role": "user", "content": context_summary})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response: str = completion.choices[0].message.content

        return f"[{self.name}]: {response}"
