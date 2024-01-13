from src.agents.Agent import Agent
from src.utils import ConsoleHelpers


class StructureAgent(Agent):
    def __init__(self, storyline: str):
        super().__init__(
            name="StructureAgent",
            role="""
                You are an experienced book author who is particularly good at structuring a book. You have the following task:
                You receive a complete story for a book as input. You are to analyse this story and divide it into meaningful chapters. Your output should have the following structure (example):
                After each Chapter content you should add a ';' to the end of the row.
                Chapter 1: "[Create an exciting title for the chapter, based on the content you have assigned to the first chapter]"
                Chapter 1 content: Here you take all the points of the story which, according to your expertise, should be in Chapter 1.;

                Chapter 2: .....
                Chapter 2 content: ....;

                Do not change or add any information to the storyline that you have received as input. The order of the story should also be maintained. You should only structure it into different chapters. 
                """
        )

        self.book_structure = self.take_input_and_generate_response(storyline)
        self.list = []

    def write_chapters_into_list(self, book_structure):
        # book_structure = str(book_structure).replace('\n', '')
        self.list = book_structure.split(';')

        for x in self.list:
            print(ConsoleHelpers.convert_to_block_text(str(x)) + "\n")
        # print(self.list)
        return self.list
