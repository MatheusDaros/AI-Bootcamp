# Lesson 10: Extending the Capabilities of GPTs

In this lesson, we will learn how to extend the capabilities of GPTs by using assistants and retrieval-augmented generation (RAG) tools.

We are going to use OpenAI Platform to create and test an assistants, managing threads and messages, and using the augmentation jobs with it. We are going to learn the practical applications of assistants and how these can be used to consistently respond to structured text generation tasks for many different threads from many users.

We are also going to learn and experiment with RAG techniques by running a local GPT model using the NVidia Chat with RTX tool. We are going to feed a local dataset to it and ask questions about information that is present in it. We are going to discover how GPTs can return information about things not present in their training data by providing the correct contextual information and instructions to retrieve it.

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
* Create an account at [OpenAI Platform](https://platform.openai.com/)
  * If you want to run the API Commands on the platform, set up [billing](https://platform.openai.com/account/billing/overview) and add at least **5 USD** credits to your account
* Optional: Download and install [NVIDIA Chat with RTX](https://www.nvidia.com/en-us/ai-on-rtx/chat-with-rtx-generative-ai/) (Windows only)
  * Check the [System Requirements](https://www.nvidia.com/en-us/ai-on-rtx/chat-with-rtx-generative-ai/) to check if your device is compatible

## Review of Lesson 09

* Types of models
* Hardware requirements and tweaking models to run in your hardware
* Overview of GPT training
* Fine-tuning GPT-2

## Overcoming the Limitations of GPTs

* What GPTs can do "out of the box"
* Giving instructions to GPTs
* Using GPTs to generate code
* Managing context and relevant information

## Using Assistants

* What is a GPT assistant
* Assistant roles and personal instructions
* Reusing an assistant for many threads
* Managing messages inside a thread
  * Using files inside threads
* Processing chat requests
* Processing instructions
* Generating codes
* Generating images
* Generating files
* Retrieving information from the web
* Retrieving information from files

## Building and Testing an Assistant with OpenAI APIs

* Practical exercises
  * Exercise 1: [Creating a simple assistant](./project/00-Create-Assistant.md) with instructions to tell engaging pirate stories
  * Exercise 2: [Creating a message thread](./project/01-Create-Message-Thread.md) with the assistant to ask for a pirate story about finding a treasure with a treasure map

## Retrieving Information

* What is RAG (Retrieval-Augmented Generation)
* Managing context size
* Retrieving relevant information from a bigger dataset
* Feeding the GPT with retrieved information

## Retrieval-Augmented Generation (RAG) Tools

* Searching the web
* Searching a file's content
* Watching a video
* Reading from PDF documents and books
* Experimentation with the NVidia [Chat with RTX](https://www.nvidia.com/en-us/ai-on-rtx/chat-with-rtx-generative-ai/) tool

## Experimenting with RAG

* Practical exercises
  * Exercise 3: Create an assistant and [Provide a File](./project/02-RAG-Assistant.md) for it to retrieve information from, and then test it with a message thread
  * Exercise 4: [Feed a local dataset](./project/03-RAG-With-Local-Dataset.md) to the NVidia's Chat with RTX tool and test it with a message

## Next Steps

* Comparing models
* Other models
* Code generation models
* Image generation models
* Generating images with AI
* Introduction to Stable Diffusion
