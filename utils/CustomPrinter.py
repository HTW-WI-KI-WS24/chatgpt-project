import InputChecker
from utils import TextFormatter


def custom_print(
        text: str,
        should_display_that_process_can_be_repeat: bool = False,
        should_display_that_process_can_be_skipped: bool = False
):
    print()
    has_displayed_additional_information = False

    if should_display_that_process_can_be_skipped:
        if not has_displayed_additional_information:
            print_of_length(TextFormatter.approximate_line_length + 5)

        print(f"   If you would like to continue with the next process, please enter \"{InputChecker.skip_command}\".")
        has_displayed_additional_information = True

    if should_display_that_process_can_be_repeat:
        if not has_displayed_additional_information:
            print_of_length(TextFormatter.approximate_line_length + 5)

        print(f"   If you wish to repeat this process, please enter \"{InputChecker.repeat_command}\".")
        has_displayed_additional_information = True

    if has_displayed_additional_information:
        print_of_length(TextFormatter.approximate_line_length + 5)

    print(TextFormatter.format_text(text))


def print_of_length(length: int):
    line_string = ""

    for i in range(int(length/2)):
        line_string += "=-"

    if length % 2 == 0:
        line_string = line_string[:-1] + "="
    else:
        line_string += "="

    print(line_string)
