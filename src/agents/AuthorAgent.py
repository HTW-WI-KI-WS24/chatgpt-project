from src.agents.Agent import Agent


class AuthorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="AuthorAgent",
            role="""
                You are a proficient book author specializing in crafting chapters based on a 
                predefined structure. Your creative process involves receiving input that includes the chapter's 
                structure and a summary of the preceding chapter. Your task is to seamlessly integrate these elements 
                into the existing narrative, maintaining a consistent writing style throughout. Try to take advantage of
                the maximum amount of words you can output. The chapters should be about 2.000 words.
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.model = "gpt-4-1106-preview"
        # self.context.append({"role": "user", "content": book_structure_list})
        self.recent_chapters_summary = ''
        self.context.append({"role": "user", "content": self.recent_chapters_summary})

    def write_chapter(self, chapter_structure):
        chapter_content = self.take_input_and_generate_response(chapter_structure)
        self.write_chapter_into_textfile(chapter_content)
        self.summarize_chapter(chapter_content)
        return chapter_content

    def write_chapter_into_textfile(self, chapter_content):
        f = open("test.txt", "a")
        f.write(str(chapter_content) + "\n")
        f.close()

        # open and read file after appending
        f = open("test.txt", "r")
        print(f.read())

    def summarize_chapter(self, chapter_content):
        self.recent_chapters_summary = self.take_input_and_generate_response("Please summarize the the given content "
                                                                             "of the chapter. The summary should "
                                                                             "contain all the key points of the "
                                                                             "chapter so that there can be made a "
                                                                             "fluid transition to the following "
                                                                             "chapter. Content: " + str(chapter_content))
