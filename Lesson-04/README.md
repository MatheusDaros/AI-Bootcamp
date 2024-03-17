# Lesson 04: Using OpenAI APIs

In this lesson we will explore how to use the OpenAI APIs to run Generative AI tasks in a remote server using python scripts with the `openai` package.

We will interact with some different endpoints of the OpenAI API, like the `chat`,`image` and `vision`, to test what are the capabilities of the Generative AI models available in the platform. We will compare some different models for these tasks and see how they perform in different scenarios.

In future lessons we will run some of these models in our own devices, but for now we will use the OpenAI platform to run the models to make the learning process easier.

We will expand in the Text Generation topic by studying how different `prompt` techniques can be used to control and tweak the output of the Generative AI models.

## Prerequisites

* Learn how to use a shell/terminal/console/bash in your device
  * Get familiar with basic commands like `cd`, `ls` and `mkdir`
  * Learn how to execute packages, scripts and commands in your device
* Install python tools in your device
  * [Python](https://www.python.org/downloads/)
  * [Pip](https://pip.pypa.io/en/stable/installation/)
* Learn how to use `python` and `pip` commands
  * Docs: [Python](https://docs.python.org/3/)
  * Docs: [Pip](https://pip.pypa.io/en/stable/)
* Learn how to use `venv` to create and manage virtual environments
  * Docs: [Python venv](https://docs.python.org/3/library/venv.html)
* Install `git` CLI in your device
  * [Git](https://git-scm.com/downloads)
* Learn how to use `git` commands to clone repositories
  * Docs: [Git](https://git-scm.com/doc)
* Learn the basics of `python` programming language syntax
  * [Python official tutorial](https://docs.python.org/3.12/tutorial/index.html)
  * [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/)
* Create an account at [OpenAI Platform](https://platform.openai.com/)
  * If you want to run the API Commands on the platform, set up [billing](https://platform.openai.com/account/billing/overview) and add at least **5 USD** credits to your account

## Review of Lesson 03

* What are GPTs
* How GPTs works
* Capabilities and limitations
* Use cases
* Applications using GPTs
* How to use GPTs with the `transformers` package
* How to use GPTs with API calls

## OpenAI APIs

* How APIs work

  * Instead of running executions in your own device, an API call can run these executions in a remote server, over the internet
    * This is useful when the execution requires a lot of computational power, or when the execution requires a lot of data that is not available in your device
    * Sometimes you need to process sensitive data, like credentials or personal information, and you don't want to expose this data to the `client side`
      * In these cases, you can run the execution in a `remote server` and only send the results to the `client`

* Interacting with APIs over HTTP

  * APIs are a fundamental tool for accessing and manipulating resources provided by web services. The 'requests' library is most commonly used with Python. with the HTTP library installed, it is possible to construct HTTP requests, specifying the request method (GET, POST, PUT, DELETE, etc.), the API endpoint URL. After sending an HTTP request, the API will process the request and return a response. This response can contain the requested data in the response body, as well as additional metadata such as HTTP status codes and response headers

  * All of this work is carried away in a remote server, and the results are sent back to whomever asked it over the internet. This way you can execute heavy tasks with access to sensitive data without handling any of it in your device

  * The library will provide methods that will be used to construct and send HTTP requests to the API endpoints.
    For example, a request from the GET method: `response = requests.get('https://api.example.com/data')`
    To access the response:
    `print(response.text)`
    It is important to mention that some APIs require authentication, in these cases credentials will need to be included in the request; in Python, for example:
    `headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}`
    `response = requests.get('https://api.example.com/data', headers=headers)`

  * It is also possible to implement error handling, for example:

    `if response.status_code == 200:`
    `print('Request was successful')`
    `else:`
    `print('Error:', response.status_code)`

* OpenAI API
  * The OpenAI API provides access to a variety of powerful artificial intelligence models that are trained on large datasets, including text generation, image generation, and natural language recognition models. Developers can integrate AI capabilities into their applications, websites, and systems by accessing models through specific API endpoints
  * Since the use of this computation is billed, OpenAI needs to identify and authorize (or not) each person/agent doing requests to the API
    * This is done through assign a unique secret key or set of keys, which are unique to each user and must be included in every request made to the API
  * Authentication to the OpenAI API is done through the use of an API key. Each user is assigned a unique API key that must be included in every request made to the API. The API key is usually passed as an HTTP header in the request or as a query parameter
  * Each request made to the API will result in costs, that is, each computation performed on the OpenAI API is charged to the user. Costs may vary based on the type of model used, the size of the request and the response, and the amount of compute power and resources used
* Endpoints
  * Each endpoint available in the OpenAI API offers specific functionality to meet the needs of developers
  * There is not a single endpoint that can be used to access all the models and capabilities of the OpenAI services
    * Instead, there are several endpoints, each one providing access to a specific model or set of models, and each one with its own set of capabilities and requirements
  * The most common endpoints are `chat`, for text generation tasks, `audio`, for speech recognition and creation, `images`, for image generation and helpers for passing images to chat completion endpoints, and  `fine_tuning`, for creating and managing fine tuning jobs and models
    * There are many other useful endpoints for things like creating assistants, moderating text content, calculating text embeddings, and much more
    * For a full list of features, check the "Capabilities" section of the [OpenAI Platform Documentation](https://platform.openai.com/docs/overview) and the "Endpoints" section of the [API Reference](https://platform.openai.com/docs/api-reference/introduction)
* Text Generation
  * The `chat` endpoint in the OpenAI API allows users to request text generation based on provided input, which is useful for text autocompletion, generating content for writing, and language translation
  * The [Chat Completions](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) tasks require passing at least a `model definition` and a `message` in the `request body`
    * In the body you can pass many other parameters like model configurations for things like `temperature` and `max_tokens` and requests options for things like `stream` and `user`
  * The response object will contain the generated text inside an object called `choices`, as well as additional metadata such as the `model` used, the `system_fingerprint` of the GPT version, and the `usage` statistics of the API request
* Image Generation
  * The `image` endpoint in the OpenAI API allows users to request the generation of images based on a given input, it is possible to provide a description or visual input, users ask the API to generate corresponding images based on that input, using specific artificial intelligence models for this purpose.
* Vision
  * OpenAI's `chat` endpoint allows passing one or many images as content in the request body, under the `content` object, by giving it a type of `image_url`
    * The provided images can then be used when the model is generating response by first being passed inside an _image recognition_ process, and then being used as a _context_ for the _text generation_ process
      * According to the [documentation](https://platform.openai.com/docs/guides/vision), the model is best at answering general questions about what is present in the images, but it is not that optimized to answer detailed questions about the location of certain objects in an image yet
        * For example, you can ask it what color a car is or what some ideas for dinner might be based on what is in you fridge, but if you show it an image of a room and ask it where the chair is, it may not answer the question correctly
  * You can control the `detail` parameter to specify how the model processes the image and generates its textual understanding
    * You can provide three options: `low`, `high`, or `auto`
    * By default, the model will use the `auto` setting which will look at the image input size and decide if it should use the `low` or `high` setting
      * Using `low` will enable the "low res" mode, where the model will receive a low-res 512px x 512px version of the image, and represent the image with a budget of 65 tokens
        * This allows the API to return faster responses and consume fewer input tokens for use cases that do not require high detail
      * Using `high` will enable "high res" mode, which first allows the model to see the low res image and then creates detailed crops of input images as 512px squares based on the input image size
        * Each of the detailed crops uses twice the token budget (65 tokens) for a total of 129 tokens

## Implementing OpenAI APIs Calls

* The [OpenAI Python API library](https://github.com/openai/openai-python)
* Environment setup
* Authentication
* Calling the endpoints
* Handling the responses

## Using the OpenAI Python API library

* Practical exercises
  * Exercise 1: [Experimenting models for text completion tasks](./project/00-Text-Completion-Models.md) to evaluate their performance and capabilities
    * Code and run [TextCompletionModels.py](./project/TextCompletionModels.py) in this exercise
  * Exercise 2: [Generating images with AI](./project/01-Image-Generation.md) to evaluate the performance and capabilities of the image generation models
    * Code and run [ImageGeneration.py](./project/ImageGeneration.py) in this exercise
  * Exercise 3: [Using AI for computer vision tasks](./project/02-Computer-Vision.md) to evaluate the performance and capabilities of the computer vision models
    * Code and run [ComputerVision.py](./project/ComputerVision.py) in this exercise

## Introduction to Prompt Engineering

* Why prompts are important
  * As we've seen in previous lessons, the prompt is a key element to control the output of the Generative AI models
  * For each desired _output_ there is a set of corresponding _prompts_ that can be passed to the model to get results in that _text region_
    * There is no direct way to know the exact _prompts_ that will generate the desired _output_, especially when the criteria for _desired_ are subjective and dynamic
    * The only possible way to _optimize_ the prompting process is to iteratively experiment with different _prompts_ and observe the _outputs_ to find the best combination of words in the _text space_
* Different prompts for different models
  * Each model has its own _text space functions_ and _prompting_ capabilities, so it is common to find prompts that work well for one model but not for another
  * Some models require specific structures and/or codes to be passed in the prompts to work properly
  * Some models are meant to be prompted with a text to complete, others with image bytes, other with code snippets, others with step by step instructions, and so on
    * Due to this vast variety of requirements, it's almost impossible to find a one-size-fits-all prompt guide
* General recommendations for prompt techniques
  * Specificity: Clearly defining the question or task
  * Contextual Clues: Providing relevant background information
  * Direct Instructions: Stating explicitly what type of response is needed
  * Tone Setting: Indicating the desired style or tone of the response
* Other techniques
  * Phrasing Variations: Experimenting with different ways of phrasing the same question to see which elicits the best response
  * Example Providing: Giving examples of the expected output
  * Guided Queries: Asking follow-up questions to narrow down the focus
  * Role-playing: Asking the AI to assume a specific role or perspective to tailor its responses
  * Constraints Setting: Specifying any limitations or constraints for the response, such as word count, format, or specific points to include or avoid
  * Iterative Refinement: Revising and refining the prompt based on the AI’s initial response to steer it in the desired direction

## Testing Prompts

* Practical exercises
  * Exercise 4: [Testing prompts for text completion tasks](./project/03-Testing-Prompts.md) to evaluate the performance and capabilities of different prompts
    * Code and run [TestingPrompts.py](./project/TestingPrompts.py) in this exercise
  * Exercise 5: Building [Chef GPT script](./project/04-Chef-GPT.md) to suggest recipes and cooking tips based in a pre-configured prompt
    * Code and run [ChefGPT.py](./project/ChefGPT.py) in this exercise

## Weekend Project

For consolidating the knowledge acquired in this week, the students should complete the following project:

1. Create a github repository for your project
2. Add all members of your group
3. Create a README.md file with the description of your project
4. Extend the `Chef GPT script` with a prompt to give some sort of "personality" to your AI chef

   * For example, you could make your chef a "young and spirited Indian cook that loves to make Biryani" or a "wise and experienced Italian chef that loves to make pasta"

5. Create one script for each member of your group with a different prompt setting

   * To make things interesting, you could make each member of your group a different "personality" for the AI chef, for example a "sassy and sarcastic vegan French chef" an a "fun and energetic Mexican chef that loves to make tacos"

6. Make the prompt in the script react to three possible different inputs: suggesting dishes based on ingredients, giving recipes to dishes, and criticizing the recipes given by the user input

   * If the user passes a different prompt than these three scenarios, the AI should deny the request

7. Create a `main.py` script that will call the different scripts based on the user input

8. Experiment passing a list of ingredients for one script, then ask a recipe for that dish to another script, and then criticize the recipe given by the last script with a third script

9. Create a report with the results of the experiment and the different outputs of the AI chefs

10. Submit your project in the submission form

>You should find your group in the [Discord](https://discord.gg/encodeclub) AI Bootcamp Channel
>>If you can't find your group, please contact the program manager through Discord or email

## Next Steps

* Exploring other API Calls
* Exploring other providers
* Creating Frontend applications for your AI tasks
* Running models in your own hardware
