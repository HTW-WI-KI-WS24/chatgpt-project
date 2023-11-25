import InputChecker
from utils import TextFormatter


def custom_print(
        text: str,
        should_display_that_process_can_be_repeat: bool = False,
        should_display_that_process_can_be_skipped: bool = False
):
    print()
    if should_display_that_process_can_be_skipped:
        print(f"If you would like to skip to the next process, please enter \"{InputChecker.skip_command}\".")
    if should_display_that_process_can_be_repeat:
        print(f"If you would like to repeat this process, please enter \"{InputChecker.repeat_command}\".")
    print("---")
    print(TextFormatter.format_text(text))
