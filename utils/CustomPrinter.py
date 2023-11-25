from utils import TextFormatter


def custom_print(text: str):
    print("\nIf you would like to skip to the next process, please enter \"skip\".")
    print("---")
    print(TextFormatter.format_text(text))
