approximate_line_length = 100


def format_text(text: str):
    text = text.strip()
    words = text.split()

    formatted_text = ""
    number_of_chars_in_current_line = 0

    for word in words:
        if number_of_chars_in_current_line > approximate_line_length:
            formatted_text += "\n"
            number_of_chars_in_current_line = 0

        formatted_text += word + " "

        for char in word:
            number_of_chars_in_current_line += 1
        number_of_chars_in_current_line += 1  # account for spaces

    formatted_text += "\n"
    return formatted_text
