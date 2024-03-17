from openai import OpenAI

client = OpenAI()

messages = [
     {
          "role": "user",
          "content": input("Type your prompt:\n"),
     }
]

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")