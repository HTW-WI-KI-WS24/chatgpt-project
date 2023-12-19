from src.utils import InputChecker


def print_command_list(
        can_process_be_skipped: bool = True,
        can_process_be_repeat: bool = True
):
    print()
    print_line()

    if can_process_be_skipped:
        print(f"\tIf you would like to continue with the next process, please enter \"{InputChecker.skip_command}\".")

    if can_process_be_repeat:
        print(f"\tIf you wish to repeat this process, please enter \"{InputChecker.repeat_command}\".")

    print_line()


def convert_to_block_text(
        text: str,
        approximate_line_length: int = 100
):
    words: list[str] = text.strip().split()

    block_text: str = ""
    number_of_chars_in_current_line: int = 0

    for word in words:
        if number_of_chars_in_current_line > approximate_line_length:
            block_text += "\n"
            number_of_chars_in_current_line = 0

        block_text += word + " "

        for char in word:
            number_of_chars_in_current_line += 1
        number_of_chars_in_current_line += 1  # account for spaces

    return block_text


def print_line(length: int = 119) -> None:
    line_string = ""

    for i in range(int(length/2)):
        line_string += "=-"

    if length % 2 == 0:
        line_string = line_string[:-1] + "="
    else:
        line_string += "="

    print(line_string)


def make_cursive(text: str) -> str:
    return f"\x1B[3m{text}\x1B[0m"


def create_space(number_of_lines: int = 3):
    for i in range(number_of_lines):
        print()


def press_enter_to_continue() -> None:
    input(f"\nPress {make_cursive("Enter")} to continue...")
