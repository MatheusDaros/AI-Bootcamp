# Lesson 07: Using Text Generation WebUI

In this lesson, we will delve into the practical application of Generative AI by exploring the Text Generation WebUI tool. Text Generation WebUI offers a user-friendly interface to interact with various [GPT models](https://huggingface.co/models), allowing us to generate text for a multitude of tasks and scenarios.

By abstracting away complexities and providing a streamlined workflow, this tool empowers us to leverage the power of Generative AI more effectively.

Prior to diving into this lesson, it is recommended to have a basic understanding of developer tools and a rudimentary grasp of Python programming syntax. With these prerequisites in place, we can explore the capabilities of Text Generation WebUI and harness its potential to address real-world challenges through AI-driven text generation.

## Prerequisites

* Learn how to use a shell/terminal/console/bash on your device
  * Get familiar with basic commands like `cd`, `ls` and `mkdir`
  * Learn how to execute packages, scripts and commands on your device
* Install python tools on your device
  * [Python](https://www.python.org/downloads/)
  * [Pip](https://pip.pypa.io/en/stable/installation/)
* Learn how to use `python` and `pip` commands
  * Docs: [Python](https://docs.python.org/3/)
  * Docs: [Pip](https://pip.pypa.io/en/stable/)
* Learn how to use `venv` to create and manage virtual environments
  * Docs: [Python venv](https://docs.python.org/3/library/venv.html)
* Install `git` CLI on your device
  * [Git](https://git-scm.com/downloads)
* Learn how to use `git` commands to clone repositories
  * Docs: [Git](https://git-scm.com/doc)
* Install the [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui?tab=readme-ov-file#how-to-install) tool on your device
  * Follow the instructions on the repository to install the tool
  * Make sure you have the necessary dependencies and configurations on your device
* Download a compatible GPT model and place in the correct `models` folder for Text Generation WebUI

## Review of Lesson 06

* Running models
* Capabilities of the Vercel NextJS AI SDK
* Generative AI Tools
* Creating the frontend code
* Getting started with the Text Generation WebUI

## Exploring Different Models

In the last lesson we saw how to use Text Generation WebUI application to run GPT models in our own devices for processing text generation tasks.

Today, we're going to explore more of the many features of this tool and see how we can use it to run different models and tasks.

* Downloading Models using the [Model Hub](https://huggingface.co/models) from Hugging Face
* Model configurations
* Model loaders
* Selecting models
* Finding good instruction-following models
* Running different tasks

## Chatting with a Local GPT Model

* Practical exercises
  * Exercise 1: [Using Chat Text Generation](./project/00-Chat-Text-Generation.md)
  * Exercise 2: [Using Instruct Text Generation](./project/01-Instruct-Text-Generation.md)
  * Exercise 3: [Using Chat-Instruct Text Generation](./project/02-Chat-Instruct-Text-Generation.md)
  * Exercise 4: [Using the Notebook mode](./project/03-Notebook-Mode.md)

## More Features

* Using [Extensions](https://github.com/oobabooga/text-generation-webui/wiki/07-%E2%80%90-Extensions#built-in-extensions)
* Using the [API flag](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API)
* [Fine tuning](https://github.com/oobabooga/text-generation-webui/wiki/05-%E2%80%90-Training-Tab) models

## Replacing the OpenAI APIs

Now that we have a tool to run GPT models on our own devices, we can run the `Text Generation` tasks services and serve them with a local API.

By using the built-in OpenAI API Extension from Text Generation WebUI, we can now replace the calls to OpenAI APIs inside our scripts and applications with calls to this local API.

* Practical exercise
  * Exercise 5: [Using the Text Generation WebUI API](./project/04-Using-API.md) as a replacement for OpenAI APIs in a python script

## Next Steps

* Exploring more features of Text Generation WebUI
* Experimenting with local GPTs
* Testing different prompting techniques
* Building an application using the local API
