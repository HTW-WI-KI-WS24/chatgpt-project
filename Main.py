from openai import OpenAI
from agents.CentralAgent import CentralAgent

# OpenAI Client
client = OpenAI()

# Agents
central_agent = CentralAgent()

active_agent = central_agent

def format_text(text: str):
    approximate_line_length = 80

    txt = text.strip()

    words = txt.split()

    formatted_text = ""

    number_of_chars_in_current_line = 0
    for word in words:
        if number_of_chars_in_current_line > approximate_line_length:
            formatted_text += "\n"
            number_of_chars_in_current_line = 0
        else:
            formatted_text += word + " "

        for char in word:
            number_of_chars_in_current_line += 1
        number_of_chars_in_current_line += 1 # account for spaces

    formatted_text += "\n"

    return formatted_text

while True:
    print(format_text(active_agent.get_opening_statement()))
    user_request = input()
    print(format_text(active_agent.get_response(user_request)))
