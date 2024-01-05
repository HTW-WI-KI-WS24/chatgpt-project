from utils import ConsoleHelpers

welcome_message: str = ("[BookGPT]: Welcome! "
                        "This software supports you in writing any book you can imagine. "
                        "You will be lead through various processes by a number of "
                        "professional book-writers, aiming to make writing your own "
                        "book as simple as possible for you.")


def introduce_application() -> None:
    print(ConsoleHelpers.convert_to_block_text(welcome_message))
    ConsoleHelpers.press_enter_to_continue()
