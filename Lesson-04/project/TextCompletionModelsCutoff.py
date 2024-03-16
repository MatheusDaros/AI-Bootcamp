from openai import OpenAI

client = OpenAI()

messages =[
    {
        "role": "user",
        "content": "When did the current war between Russia and Ukraine started?",
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