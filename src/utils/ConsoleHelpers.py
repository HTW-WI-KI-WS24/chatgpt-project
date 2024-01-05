from src.utils import InputChecker


def print_command_list(
        can_process_be_skipped: bool = True,
        can_process_be_repeat: bool = True
):
    print()
    print_line()

    if can_process_be_skipped:
        print(f"\tIf you would like to skip the current process, please enter \"{InputChecker.skip_command}\".")

    if can_process_be_repeat:
        print(f"\tIf you wish to repeat the current process, please enter \"{InputChecker.repeat_command}\".")

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


def create_space(number_of_lines: int = 5):
    for i in range(number_of_lines):
        print()


def press_enter_to_continue(empty_lines_before_press_enter_request: int = 1) -> None:
    for i in range(empty_lines_before_press_enter_request):
        print()

    input(f"Press {make_cursive("Enter")} to continue...")


def print_waiting_for_generation_message(
        empty_lines_before_generating_message: int = 1,
        empty_lines_after_generating_message: int = 1
) -> None:
    for i in range(empty_lines_before_generating_message):
        print()

    print(make_cursive("generating..."))

    for i in range(empty_lines_after_generating_message):
        print()


def get_user_input(empty_lines_before_input_request: int = 1) -> str:
    for i in range(empty_lines_before_input_request):
        print()

    print("Type here: ", end="")
    user_input: str = input()
    return user_input
