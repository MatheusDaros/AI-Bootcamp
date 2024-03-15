from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "user",
        "content": 'Generate an HTML file with a simple chat interface and include a script to send the message somewhere when you click the "generate" button',
    }
]

models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-0125-preview"]

for model in models:
    print(f"\nGenerating chat completion with {model}:\n")
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    print("\n\n---\n")