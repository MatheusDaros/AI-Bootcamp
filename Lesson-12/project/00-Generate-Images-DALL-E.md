# Generating Images with DALL-E using OpenAI's API

1. Make sure that you have set up your keys correctly with the exercise `01-OpenAI-Key.md` from Lesson 01

2. Make sure that your `venv` is activates

3. Run the following code on your terminal:

   ```bash
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

   * By default, this will try to use the `OPENAI_API_KEY` environment variable to create this client

   * You can customize the logic by doing an explicit definition like this:

     ```python
     import os
     from openai import OpenAI
 
     client = OpenAI(
         api_key=os.environ.get("OPENAI_API_KEY"),
     )
     ```

     * Here you can change `api_key` to any value that you want to use

     * Have caution if you prefer to hardcode your key in this file, since this could lead to you inadvertently sharing your key with others

7. Call the [Image Generations](https://platform.openai.com/docs/guides/images) endpoint in the `client` with the following parameters:

   ```python
   response = client.images.generate(
       model="dall-e-2",
       prompt=input("Describe the image you want to generate:"),
       size="512x512",
       n=1,
    )
   ```

   * The `model` parameter is the name of the model that you want to use to generate the image
     * The models available to use from OpenAI API are listed in the [Models](https://platform.openai.com/docs/models/overview) API documentation
   * The `prompt` parameter describes the desired image
   * The `size` parameter indicates the desired dimensions of the image
     * See supported sizes in the [Create Image](https://platform.openai.com/docs/api-reference/images/create) documentation
   * The `quality` parameter determines the image quality
     * See supported qualities in the [Create Image](https://platform.openai.com/docs/api-reference/images/create) documentation
   * The `n` parameter specifies the number of images to generate

8. Print the URL of the generated image

   ```python
   print(response.data[0].url)
   ```

9. Run the file

   ```bash
   # Linux/MacOS
   python <filename>.py
   ```

   ```bash
   # Windows
   py <filename>.py
   ```

10. Check the output

    * You should see the URL of the generated image printed on your terminal

    * Copy the URL and paste it into your browser to view the generated image

11. Experiment with the [Image Generations API Parameters](https://platform.openai.com/docs/api-reference/images) to test how the model behaves with different inputs and configurations

>View more information about the OpenAI API at <https://platform.openai.com/docs> and the OpenAI Python Package at <https://github.com/openai/openai-python>
