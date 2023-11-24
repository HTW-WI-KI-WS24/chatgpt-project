from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts in " +
                                  "a creative but concise way."}
]


def new_chat():
    for message in messages[1:]:
        messages.pop(message)


def ask(user_input):
    messages.append({"role": "user", "content": user_input})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = completion.choices[0].message.content
    print(response + "\n-----")
    messages.append({"role": "assistant", "content": response})


ask("write a short poem about the singleton design pattern")


ask("make it shorter")
