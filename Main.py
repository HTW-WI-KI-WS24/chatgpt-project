from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts in a creative but concise way."},
    {"role": "user", "content": "Compose a short poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
