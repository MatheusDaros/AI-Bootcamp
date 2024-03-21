# Testing Different Prompts

1. Make sure that you have set up your keys correctly with the exercise `01-OpenAI-Key.md` from Lesson 01

2. Make sure that your `venv` is activated

3. Run the following code on your terminal:

   ```text
   pip install openai
   ```

   * This command will install the `openai` [API Package](https://github.com/openai/openai-python) on your environment

4. Create a new Python file

   * Create a new file on your favorite code editor or simply run `touch <filename>.py` on your terminal (Linux/MacOS) or `type nul > <filename>.py` on your terminal (Windows)

   * Remember to replace `<filename>` with the name of your file

5. Import the `openai` module on your file

   ```python
    from openai import OpenAI
    ```

   * This `client` can abstract all of the complexities of consuming the OpenAI API endpoints, like handling the authentication, the request and response formats, synchronous and asynchronous requests, and many other features

   * To use this library correctly, all you need to do is to understand well the [API parameters](https://platform.openai.com/docs) that you want to consume

6. Create a new `client` instance

   ```python
    client = OpenAI()
    ```

   * By default, this will try yo use the `OPENAI_API_KEY` environment variable to create this client

   * You can customize the logic by doing an explicit definition like this:

   ```python
   import os
   from openai import OpenAI
   client = OpenAI(
       api_key=os.environ.get("OPENAI_API_KEY"),
   )
   ```

   * Here you can change `api_key` to any value that you want to use

   * Have caution if you prefer to hardcode your key in this file, since this could lead yo you inadvertently sharing your key with others

7. Receive the `prompt` message from the user and store it in a variable

   ```python
    messages = [
         {
              "role": "user",
              "content": input("Type your prompt:\n"),
         }
    ]
    ```

    * The `input` function will ask the user to type a prompt message in the console

8. Specify the model to use:

   ```python
   model = "gpt-3.5-turbo"
   ```

9. Call the [Chat Completion](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) endpoint in the `client` in a loop with the following parameters:

    ```python
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    ```

10. Run the file

    ```text
    # Linux/MacOS
    python <filename>.py
    ```

    ```text
    # Windows
    py <filename>.py
    ```

11. Test many prompts to see how the model responds to each one

    * You can test the following prompts:

    ```text
    Type your prompt:
    What is the meaning of life?
    ```

    ```text
    Type your prompt:
    What is the best programming language?
    ```

    ```text
    Type your prompt:
    What is the best programming language for data science?
    ```

    ```text
    Type your prompt:
    What is the best programming language for web development?
    ```

12. Test more complex prompts to test the capabilities and the limits of the model

    ```text
    Type your prompt:
    Is it possible to travel faster than the speed of light?
    ```

    ```text
    Type your prompt:
    What is the best way to solve the climate change problem?
    ```

    ```text
    Type your prompt:
    Is it raining outside?
    ```

    ```text
    Type your prompt:
    Guess my name
    ```

    ```text
    Type your prompt:
    My name is Joseph Chestnut. I like Hot Dogs.
    ```

    ```text
    Type your prompt:
    Do you know my name?
    ```

    ```text
    Type your prompt:
    Do I like Hot Dogs?
    ```

    ```text
    Type your prompt:
    What is your opinion on Pineapple on pizzas?
    ```

13. Test different ways of asking the same thing for better results

    * Be specific

    ```text
    Type your prompt:
    Who is Joseph?
    ```

    ```text
    Type your prompt:
    Who is Joseph Chestnut?
    ```

    ```text
    Type your prompt:
    Who is Joseph Chestnut, the Guinness record winner?
    ```

    * Give context

    ```text
    Type your prompt:
    What should I order?
    ```

    ```text
    Type your prompt:
    I am at a Mexican restaurant. What should I order?
    ```

    ```text
    Type your prompt:
    I am at a Mexican restaurant. I am in a group of five. What should I order?
    ```

    ```text
    Type your prompt:
    I am at a Mexican restaurant. I am in a group of five. Three of us are vegetarian, one is vegan and the last is allergic to peanuts. What should I order?
    ```

    * Give examples

    ```text
    Type your prompt:
    Suggest me a good hint for using AI like a pro
    ```

    ```text
    Type your prompt:
    Suggest me a good hint for using AI like a pro. For example, suggest me ways to write better prompts by giving examples, or suggest the most efficient ways to provide data in prompts, or suggest me the best ways to use chain of thoughts in prompts.
    ```

14. Always remember that the model is not _thinking_, since it will always answer what is more _probable_ based on the data that it was trained on
