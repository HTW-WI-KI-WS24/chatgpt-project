from openai import OpenAI


class WorldAgent:
    def __init__(self):
        self.client = OpenAI()
        self.name = "WorldAgent"
        self.context = [
            {"role": "system", "content":
                """
                You are a skilled book author who is particularly good at designing worlds for books. 
                The worlds you design are well thought out. You receive input that contains data about a book, 
                which is to be written. You use this data to design a corresponding world. You have freedom in designing the world,
                as long as it is essentially related to the input. The world should not only be described superficially by you, 
                but in great detail. Important: You dont make the story of the book. You just build the empty world, where the book can 
                play in. An other agents builds the story and the character, so dont create any Informations about the protagonist and other main characters.
                Focus primarily on the description of the world and how the various elements should affect the reader. The reader should be given a feeling. 
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

    #Hier muss der zusammengefasste Input des Users, von der Konversation mit dem CentralAgent, reingeladen werden
    def generate_world(self, context):
        self.context.append({"role": "user", "content": context})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.context
        )
        response: str = completion.choices[0].message.content

        return f"[{self.name}]: {response}"

