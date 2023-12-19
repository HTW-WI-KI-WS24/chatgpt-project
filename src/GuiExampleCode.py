import time
from agents.CentralAgent import CentralAgent
from openai import OpenAI

client = OpenAI()

central_agent = CentralAgent()


chatgpt_context = [
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts in " +
                                  "a creative but concise way."}
]

chat_message_gui_labels = []

def get_chatgpt_response(user_request):
    return central_agent.generate_response(user_request)

def generate_chatgpt_response(user_request):
    user_input_textbox.delete('1.0', "end")
    display_user_request_in_gui(user_request)
    time.sleep(1)

    chatgpt_response = get_chatgpt_response(user_request)

    display_chatgpt_response_in_gui(chatgpt_response)

    chatgpt_context.append({"role": "assistant", "content": chatgpt_response})

def new_chat():
    for item in chatgpt_context[1:]: # remove everything besides the first input (which is the role assignment)
        chatgpt_context.remove(item)

    # gui
    for chat_message_label in chat_message_gui_labels:
        chat_message_label.destroy()

def display_user_request_in_gui(user_request):
    user_request_label = ctk.CTkLabel(
        chat_frame,
        corner_radius=20,
        fg_color="#3c383d",
        font=('Arial', 16, 'normal'),
        text=user_request,
        anchor="center"
    )
    user_request_label.pack(fill="x", padx=70, pady=(35, 0), ipadx=10, ipady=10)
    chat_message_gui_labels.append(user_request_label)

def display_chatgpt_response_in_gui(chatgpt_response):
    chatgpt_response_label = ctk.CTkLabel(
        chat_frame,
        corner_radius=20,
        fg_color="#383d38",
        font=('Arial', 16, 'normal'),
        text=chatgpt_response,
        anchor="center"
    )
    chatgpt_response_label.pack(fill="x", padx=70, pady=(35, 0), ipadx=10, ipady=10)
    chat_message_gui_labels.append(chatgpt_response_label)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window = ctk.CTk()
window.title("BookGPT")
window.geometry("800x600")
window.after(1, window.wm_state, "zoomed")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

chat_frame = ctk.CTkScrollableFrame(window, corner_radius=0)
chat_frame.grid(column=0, row=0, sticky="nsew")

input_frame = ctk.CTkFrame(window, corner_radius=0)
input_frame.columnconfigure(0, weight=1)
input_frame.rowconfigure(0, weight=1)
input_frame.grid(column=0, row=1, sticky="nsew")

user_input_textbox = ctk.CTkTextbox(
    input_frame,
    corner_radius=20,
    height=100,
    fg_color="gray22",
    font=('Arial', 18, 'normal')
)
user_input_textbox.grid(column=0, row=0, padx=70, pady=(70, 0), sticky="nsew")

send_request_button = ctk.CTkButton(
    input_frame,
    text="Anfrage senden",
    fg_color="#3c383d",
    command=lambda: generate_chatgpt_response(user_input_textbox.get("1.0", "end"))
)
send_request_button.grid(column=0, row=1, padx=70, pady=(20, 50), sticky="e")

new_chat_button = ctk.CTkButton(
    input_frame,
    text="Neuer Chat",
    fg_color="#3c383d",
    command=new_chat
)
new_chat_button.grid(column=0, row=1, padx=70, pady=(20, 50), sticky="w")

display_chatgpt_response_in_gui(central_agent.generate_opening_statement())

window.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
