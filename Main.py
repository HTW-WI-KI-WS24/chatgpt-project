import customtkinter as ctk
from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts in " +
                                  "a creative but concise way."}
]

chat_message_labels = []

def new_chat():
    for msg in messages[1:]:
        messages.remove(msg)
    for chat_message_label in chat_message_labels:
        chat_message_label.destroy()

def send_user_request(user_request):
    user_request_label = ctk.CTkLabel(
        chat_frame,
        corner_radius=20,
        fg_color="#3c383d",
        font=('Arial', 16, 'normal'),
        text=user_request,
        anchor="center"
    )
    chat_message_labels.append(user_request_label)
    user_request_label.pack(fill="x", padx=70, pady=(35, 0), ipadx=10, ipady=10)
    user_input_textbox.delete('1.0', "end")

    generate_chatgpt_response(user_request)

def generate_chatgpt_response(user_input):
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})
    chatgpt_response_label = ctk.CTkLabel(
        chat_frame,
        corner_radius=20,
        fg_color="#383d38",
        font=('Arial', 16, 'normal'),
        text=response,
        anchor="center"
    )
    chat_message_labels.append(chatgpt_response_label)
    chatgpt_response_label.pack(fill="x", padx=70, pady=(35, 0), ipadx=10, ipady=10)

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
    command=lambda: send_user_request(user_input_textbox.get("1.0", "end"))
)
send_request_button.grid(column=0, row=1, padx=70, pady=(20, 50), sticky="e")

new_chat_button = ctk.CTkButton(
    input_frame,
    text="Neuer Chat",
    fg_color="#3c383d",
    command=new_chat
)
new_chat_button.grid(column=0, row=1, padx=70, pady=(20, 50), sticky="w")

window.mainloop()
