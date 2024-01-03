from src.agents.Agent import Agent
from src.utils import ConsoleHelpers, InputChecker


class StructureAgent(Agent):
    def __init__(self, story: str):
        super().__init__(
            name="StructureAgent",
            role="""
                You are an experienced book author who is particularly good at structuring a book. You have the following task:
                You receive a complete story for a book as input. You are to analyse this story and divide it into meaningful chapters. Your output should have the following structure (example):
                Chapter 1: "[Create an exciting title for the chapter, based on the content you have assigned to the first chapter]"
                Chapter 1 content: Here you take all the points of the story which, according to your expertise, should be in Chapter 1.

                Chapter 2: .....
                Chapter 2 content: ....

                Do not change or add any information to the storyline that you have received as input. The order of the story should also be maintained. You should only structure it into different chapters. 
                """,
            opening_statement_instructions="Greet me and explain to me in about three sentences, what your role is."
        )
        
    def conduct_conversation(self):
        ConsoleHelpers.print_command_list()
        print(self.attach_name_and_convert_to_block_text(self.opening_statement) + "\n")

        while True:
            user_input = input()
            self.take_user_input(user_input)

            
            if InputChecker.should_skip_process(user_input):
                self.summarize_conversation()
                break
            elif InputChecker.should_repeat_process(user_input):
                self.reset_context()
                self.conduct_conversation()
                break
            else:
                response: str = self.take_input_and_generate_response(user_input)
                print("\n" + self.attach_name_and_convert_to_block_text(response) + "\n")   
        
    def write_structure(self):
        self.generate_response()

    def summarize_conversation(self):
        
        self.conversation_summary: str = self.take_input_and_generate_response(
            """
            Taking into account the user's comments and change requests, you should structure the received story into meaningful chapters, taking care to structure the book according to your role as an experienced book author who specialises in structuring books. The structure should look like this:

            Chapter 1: "[Title based on content and user notes]"
            Chapter 1 content: [Content that belongs in Chapter 1, taking into account the user's comments]

            Chapter 2: .....
            Chapter 2 content: .....

            The original story and its order are retained, but structured according to the user's comments and wishes.
            """
        )

        print("\n" + ConsoleHelpers.convert_to_block_text(self.attach_name(self.conversation_summary)))
        ConsoleHelpers.press_enter_to_continue()

    