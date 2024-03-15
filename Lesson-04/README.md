# Lesson 04: Using OpenAI APIs

In this lesson we will explore how to use the OpenAI APIs to run Generative AI tasks in a remote server using python scripts with the `openai` package.

We will interact with some different endpoints of the OpenAI API, like the `chat`,`image` and `vision`, to test what are the capabilities of the Generative AI models available in the platform. We will compare some different models for these tasks and see how they perform in different scenarios.

In future lessons we will run some of these models in our own devices, but for now we will use the OpenAI platform to run the models to make the learning process easier.

We will expand in the Text Generation topic by studying how different `prompt` techniques can be used to control and tweak the output of the Generative AI models.

## Pre-requisites

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
  * TODO: Add a brief explanation of how to interact with APIs over HTTP
  * TODO: Explain how to do this in a python script
* OpenAI API
  * TODO: Add a brief explanation of the OpenAI API
  * TODO: Explain authentication
  * TODO: Explain that every computation is billed from the user
* Endpoints
  * TODO: Add a brief explanation of the different endpoints available in the OpenAI API
* Text Generation
  * TODO: Add a brief explanation of the `text` endpoint
  * TODO: Explain the different models available
* Image Generation
  * TODO: Add a brief explanation of the `image` endpoint
* Vision
  * TODO: Add a brief explanation of the `vision` endpoint
* Other useful endpoints
  * TODO: Add a brief explanation of the other useful endpoints available in the OpenAI API, like Fine Tuning, Text to Speech, Speech to Text, Assistants and Moderation

## Implementing OpenAI APIs calls

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

## Introduction to prompt engineering

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

## Testing prompts

* Practical exercises
  * Exercise 4: [Testing prompts for text completion tasks](./project/03-Testing-Prompts.md) to evaluate the performance and capabilities of different prompts
    * Code and run [TestingPrompts.py](./project/TestingPrompts.py) in this exercise
  * Exercise 5: Building [Chef GPT script](./project/04-Chef-GPT.md) to suggest recipes and cooking tips based in a pre-configured prompt
    * Code and run [ChefGPT.py](./project/ChefGPT.py) in this exercise

## Weekend project

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

## Next steps

* Exploring other API Calls
* Exploring other providers
* Creating Frontend applications for your AI tasks
* Running models in your own hardware
