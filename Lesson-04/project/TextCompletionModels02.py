import json
from openai import OpenAI
from TenThousandTokensPrompt import ten_thousand_token_message
from TwentyThousandTokensPrompt import twenty_thousand_token_message

client = OpenAI()

messages = ten_thousand_token_message
# messages = twenty_thousand_token_message

models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-0125-preview"]

for model in models:
    print(f"\nGenerating chat completion with {model}:\n")
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        for chunk in stream:
            print(chunk.choices[0].delta.content or "", end="")
        print("\n\n---\n")
    except Exception as e:
        error_message = e.args[0]
        error_dict = error_message.split(' - ')[1]
        print(error_dict)