# Lesson 10: Extending the Capabilities of GPTs

In this lesson, we will learn how to extend the capabilities of GPTs by using assistants and retrieval-augmented generation (RAG) tools.

We are going to use the OpenAI Platform to create and test an assistant, manage threads and messages, and use augmentation jobs with it. We are going to learn about the practical applications of assistants and how they can be used to consistently respond to structured text generation tasks across many different threads from various users.

We are also going to learn and experiment with RAG techniques by running local tools. We are going to feed a local dataset to these tools and ask questions about the information present in it. We are going to discover how GPTs can return information about topics not present in their training data by providing the correct contextual information and instructions for retrieval.

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
* Create an account at [OpenAI Platform](https://platform.openai.com/)
  * If you want to run the API Commands on the platform, set up [billing](https://platform.openai.com/account/billing/overview) and add at least **5 USD** credits to your account
* Setup the `superbooga` extension in Text Generation Web UI
  * Activate [Superbooga](https://github.com/oobabooga/text-generation-webui/tree/main/extensions/superbooga) in the `Session` tab
  * Terminate the current session
  * Activate the `conda` environment in the `installer_files/env` folder
  * Navigate to the `extensions/superbooga` folder
  * Run `pip install -r requirements.txt`
  * Deactivate the `conda` environment
  * Restart the Text Generation Web UI and activate the `superbooga` extension
  * Click on `Apply flags/extensions and restart` to load the extension

## Review of Lesson 09

* Types of models
* Hardware requirements and tweaking models to run on your hardware
* Overview of GPT training
* Fine-tuning GPT-2

## Overcoming the Limitations of GPTs

* What GPTs can do "out of the box"
* Giving instructions to GPTs
* Using GPTs to generate code
* Managing context and relevant information

## Using Assistants

* What is a GPT assistant
  * AI Assistants have been around for a long time, usually in the form of chatbots programmed to respond to specific prompts or commands in a structured way
  * The use of GPTs can make these assistants more flexible and capable of handling a wider range of tasks, even sometimes for things that they weren't explicitly trained to do
  * This works for both processing the input from the user to determine the intent from it, and also for executing the task that the assistant is programmed to serve according to that specific intent
  * Different from running a normal chat or instruction task in a GPT, an assistant can be pre-configured and re-used in many different threads and messages for a consistent experience between users
    * Also these assistants can be enhanced with access to functions that widen their capabilities, like retrieving information from the web or from files, or even sending API calls to certain endpoints
* Assistant roles and personal instructions
  * An assistant can be configured to respond to specific prompts or commands in a structured way to provide consistent and helpful responses to users
  * Instead of relying in the ability of the end user to provide the correct prompt to communicate the desired intent, the assistant can be programmed to understand the intent from the user's input and execute the task accordingly
    * It's even possible to program the assistant to ask for more information if the input is not clear enough to determine the intent, based on the criteria of "clarity" most associated with the terms used in the input according to the training data
  * After configured, the assistants can respond to many different threads for different users, without mixing them up or losing context between them
    * This is possible because the assistant can be programmed to manage the context of each thread and message, and also to manage the information that is relevant to each thread
    * That way, every user can have a personalized experience with the assistant, based on each message and thread that they are interacting with
* Managing messages inside a thread
  * The assistant can be programmed to manage the messages inside a thread, to keep track of the context and the information that is relevant to each thread, without ever mixing them up
* Using files inside threads
  * The assistant can be programmed to use files inside threads, to retrieve information from them and to generate responses based on the content of the files
  * Instead of including the whole file contents in the context of the prompt, the assistant can be programmed to _retrieve_ the information from the file only when it's needed, and _augmenting_ the generation process with the fragments of this data that are more relevant to the current prompt
    * This allows the assistant to keep the context size manageable even when receiving large files to process
* Processing chat requests
  * The assistant can be programmed to process chat requests, to generate responses based on the content of the messages and the context of the thread
  * Instead of generating responses based on the last message only, the assistant can be programmed to generate responses based on the whole context of the thread, including the messages that were sent before the current one
    * This allows the assistant to generate more consistent and relevant responses, based on the whole conversation that is happening in the thread
* Processing instructions
  * The assistant can be programmed to process instructions from the end user and combine them with the pre-programmed instructions to generate responses and actions based on the combined instructions
* Generating codes
  * A very common use for such assistants is to generate code snippets based on the user's input, to help completing code scripts or even to find solutions for specific programming problems on the files that the user is providing to the assistant
* Generating images
  * Another common use for such assistants is to generate images based on the user's input by triggering specific functions that requests the generation of images from a model that is capable of doing so
* Generating files
  * Assistants can also be programmed to generate files for the user to download
    * For example the assistant could automatically provide a `pdf` version of the chat or even an `csv` table with a summary of some financial data that the user is requesting
* Retrieving information from the web
  * The _retrieval_ functions are not limited to the files that the user provides, but they could also be used to retrieve information from the web, like searching for specific terms or topics on the internet and providing the results to the user

## Building and Testing an Assistant with OpenAI APIs

OpenAI [Assistants](https://platform.openai.com/docs/assistants/overview) provide a quick and easy way to set up and test custom-made assistants powered by GPT models. The assistants can be programmed to respond to specific prompts or commands in a structured way to provide consistent and helpful responses to users.
OpenAI Assistants are currently enabled with a good set of [Useful Tools](https://platform.openai.com/docs/assistants/tools) for things like interpreting code, knowledge retrieval, running functions (like getting the weather of a city or similar tasks), and more.

* Practical exercises
  * Exercise 1: [Creating a simple assistant](./project/00-Create-Assistant.md) with instructions to tell engaging pirate stories
  * Exercise 2: [Creating a message thread](./project/01-Create-Message-Thread.md) with the assistant to ask for a pirate story about finding a treasure with a treasure map

## Retrieving Information

* What is RAG (Retrieval-Augmented Generation)
  * RAG is a technique that combines the capabilities of GPTs with the ability to retrieve information from external sources, like files, web pages, videos, books, and other documents
  * This allows the GPT to generate responses based on the content of these external sources, even when the information is not present in the training data of the model
* Managing context size
  * If the whole information from the external source is included in the context of the prompt, the GPT may not be able to generate responses based on it, because the context size is limited
  * Instead of including the whole information in the context, the GPT can be programmed to automatically select fragments of the provided augmenting data that are more relevant to the current prompt
    * This allows the GPT to generate responses based on the content of the external sources of huge sizes, without exceeding the context size limit when generating the responses
* Retrieving relevant information from a bigger dataset
  * The provided data are divided into _chunks_ and stored in a database in an organized way
    * All of the chunks are indexed and their embeddings are calculated to form some sort of _metadata_ that relates to the information they contain
  * When a prompt is given to the GPT, it compares the chunks to the prompt and selects the most relevant ones to be included in the context of the prompt
    * A vector search calculates the embeddings of the indexed chunks against those of the prompt, and selects the most similar chunks to be included in the context of the prompt
* Feeding the GPT with retrieved information
  * When the chunks are appended to the context, the model's fine-tuning for instructions allows it to modify its behavior to generate responses based on the content of the chunks

## Retrieval-Augmented Generation (RAG) Tools

* Searching the web
* Searching a file's content
* Watching a video
* Reading from PDF documents and books
* Example tool (windows only): NVidia [Chat with RTX](https://www.nvidia.com/en-us/ai-on-rtx/chat-with-rtx-generative-ai/)
* Another example tool (python): [SuperBIG](https://github.com/kaiokendev/superbig)

## Experimenting with RAG

* Practical exercises
  * Exercise 3: Create an assistant and [Provide a File](./project/02-RAG-Assistant.md) for it to retrieve information from, and then test it with a message thread
  * Exercise 4: [Feed a local dataset](./project/03-RAG-With-Local-Dataset.md) to superbooga extension and test it with a message

## Next Steps

* Comparing models
* Other models
* Code generation models
* Image generation models
* Generating images with AI
* Introduction to Stable Diffusion
