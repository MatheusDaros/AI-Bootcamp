# Lesson 07: Using Text Generation WebUI

In this lesson, we will delve into the practical application of Generative AI by exploring the Text Generation WebUI tool. Text Generation WebUI offers a user-friendly interface to interact with various [GPT models](https://platform.openai.com/docs/models), allowing us to generate text for a multitude of tasks and scenarios.

By abstracting away complexities and providing a streamlined workflow, this tool empowers us to leverage the power of Generative AI more effectively.

Prior to diving into this lesson, it is recommended to have a basic understanding of developer tools and a rudimentary grasp of Python programming syntax. With these prerequisites in place, we can explore the capabilities of Text Generation WebUI and harness its potential to address real-world challenges through AI-driven text generation.

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
* Basic knowledge about Artificial Intelligence (AI)
  * [OpenAI Platform Introduction](https://platform.openai.com/docs/introduction)

## Review of Lesson 06

* Running models 
* Capabilities of the Vercel NextJS AI SDK
* Generative AI Tools
* Creating the frontend code


## Exploring different models

In the last lesson we've seen how to use Text Generation WebUI application to run GPT models in our own devices for processing text generation tasks.

Today we're going to explore more of the many features of this tool and see how we can use it to run different models and tasks.

* Downloading Models using the [Model Hub](https://github.com/oobabooga/text-generation-webui/wiki/04-%E2%80%90-Model-Tab#download-model-or-lora) from Hugging Face
* Model configurations
* Model loaders
* Selecting models
* Finding good instruction-following models
* Running different tasks

## Chatting with a local GPT model

* Practical exercises
  * Exercise 1: [Using Chat Text Generation](./project/00-Chat-Text-Generation.md)
  * Exercise 2: [Using Instruct Text Generation](./project/01-Instruct-Text-Generation.md)
  * Exercise 3: [Using Chat-Instruct Text Generation](./project/02-Chat-Instruct-Text-Generation.md)
  * Exercise 4: [Using the Notebook mode](./project/03-Notebook-Mode.md)

## More features

* Using [Extensions](https://github.com/oobabooga/text-generation-webui/wiki/07-%E2%80%90-Extensions#built-in-extensions)
* Using the [API flag](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API)
* [Fine tuning](https://github.com/oobabooga/text-generation-webui/wiki/05-%E2%80%90-Training-Tab) models

## Replacing the OpenAI APIs

Now that we have a tool to run GPT models in our own devices, we can run the `Text Generation` tasks services and serve these with a local API.

By using the built-in OpenAI API Extension from Text Generation WebUI, we can now replace the OpenAI APIs calls inside our scripts and applications to call this local API.

* Practical exercises
  * Exercise 5: [Using the Text Generation WebUI API](./project/04-Using-API.md) as a replacement for OpenAI APIs in a python script

## Next steps

* Deepening your understanding of a _prompt_ and its role in guiding AI-generated text
* Familiarizing yourself with the concept of inference in the context of AI models
* Exploring the usage of OpenAI APIs for executing GPTs and other AI tasks
* Quality and accuracy of text generation
* Building applications

