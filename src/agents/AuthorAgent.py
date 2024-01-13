from src.agents.Agent import Agent


class AuthorAgent(Agent):
    def __init__(self, book_structure_list: str):
        super().__init__(
            name="AuthorAgent",
            role="""
                You are a proficient book author specializing in crafting chapters based on a 
                predefined structure. Your creative process involves receiving input that includes the chapter's 
                structure and a summary of the preceding chapter. Your task is to seamlessly integrate these elements 
                into the existing narrative, maintaining a consistent writing style throughout.
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        self.context.append({"role": "user", "content": book_structure_list})
        self.recent_chapters_summary = ''

    def write_chapter(self, chapter_structure):
        chapter_content = self.take_input_and_generate_response(chapter_structure)
        self.summarize_chapter(chapter_content)
        return chapter_content

    def write_chapter_into_textfile(self, chapter_content):
        f = open("test.txt", "a")
        f.write(chapter_content)
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
                                                                             "chapter. Content: " + chapter_content)
