# Lesson 06: Using GPT Models in Your Own Device

In this lesson we're going to learn and practice more on building applications with the NextJS framework and using the Vercel NextJS AI SDK to perform AI text Generation tasks.

We're going to explore how AI tools can help developers to generate code snippets or even full applications, and were're going to evaluate how helpful or how accurate these tools can be.

By the end of this lesson we're going to learn that all of the AI APIs we've been using from OpenAI and similar companies can be run in our own devices, and we're going to learn in practice how to do that for text generation tasks using a developer tool called Text Generation WebUI.

## Pre-requisites

* Learn how to use a shell/terminal/console/bash in your device
  * Get familiar with basic commands like `cd`, `ls` and `mkdir`
  * Learn how to execute packages, scripts and commands in your device
* Install Node.js in your device
  * [Node.js](https://nodejs.org/en/download/)
* Learn how to use `npm` and `npx` commands
  * Docs: [npm](https://docs.npmjs.com/)
  * Docs: [npx](https://www.npmjs.com/package/npx)
* Learn how to use `npm install` and how to deal with `node_modules` folder
  * Docs: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
* Install `git` CLI in your device
  * [Git](https://git-scm.com/downloads)
* Learn how to use `git` commands to clone repositories
  * Docs: [Git](https://git-scm.com/doc)
* Learn the basics of `javascript` programming language syntax
  * [javascript official tutorial](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  * [Learn X in Y minutes](https://learnxinyminutes.com/docs/javascript/)
* Learn the basics of `typescript` programming language syntax
  * [typescript official tutorial](https://www.typescriptlang.org/docs/)
  * [Learn X in Y minutes](https://learnxinyminutes.com/docs/typescript/)
* Install python tools in your device
  * [Python](https://www.python.org/downloads/)
  * [Pip](https://pip.pypa.io/en/stable/installation/)
* Learn how to use `python` and `pip` commands
  * Docs: [Python](https://docs.python.org/3/)
  * Docs: [Pip](https://pip.pypa.io/en/stable/)
* Learn how to use `venv` to create and manage virtual environments
  * Docs: [Python venv](https://docs.python.org/3/library/venv.html)
* Create an account for using [Vercel V0](https://v0.dev/)
  * Using a free plan is enough for this lesson
* Setup your OpenAI ket at [MakeReal](https://makereal.tldraw.com/)
  * Follow [this tutorial](https://tldraw.notion.site/Make-Real-Help-93be8b5273d14f7386e14eb142575e6e) if you have questions

## Review of Lesson 05

* Building applications
* Using frameworks
* Vercel NextJS AI SDK
* Calling OpenAI text generations APIs inside the application

## Adding features to the Frontend

Last lesson we've seen how to use the Vercel NextJS AI SDK to create a simple web application that requests ChatGPT model to generate text remotely using API calls.

In our last exercise we added a page to chat with a "Chef GPT" that could give us recipes for some dishes.

Let's explore more on the capabilities of the Vercel NextJS AI SDK and add more AI features to our web application.

* Practical exercises
  * Exercise 1: [Generating images for the dishes](./project/00-Generating-Images.md) to understand how to use OpenAI APIs for image generation
    * Edit the project created in the last exercise of previous lesson to add the new features
  * Exercise 2: [Generating audio instructions for the recipes](./project/01-Generating-Audio.md) to understand how to use OpenAI APIs for text-to-speech
    * Edit the project created in the last exercise of previous lesson to add the new features

## Generating frontend code with AI

To speed up the process of creating the frontend code for our web application, we can use Generative AI Tools to generate the code for us.

Not only tools like ChatGPT and Copilot can help developers to gain efficiency, but also they can generate big chunks of code that can be used as a starting point for software projects.

Unfortunately the accuracy of these tools is not perfect, and the generated code may require some (or lots of) adjustments and improvements. But often the generated code can be a good starting point for developers to understand how to implement a feature or a functionality.

A tool that stands out for this purpose is [v0](https://v0.dev/), from Vercel. `v0` is a web tool that generates frontend code based on a simple description of the desired layout and functionality.

Another very helpful tool is [MakeReal](https://makereal.tldraw.com/) from TLDraw. `MakeReal` is a web tool that generates frontend code based on a simple descriptions and crude drawings of the desired layout and elements.

These tools can greatly help developers to create the frontend code for their web applications, and they can be used to generate the code for the exercises of this lesson.

> Be advised that the generated code may require severe adjustments and improvements to work properly. Do never rely blindly on AI generated code.

## Running models locally

As we've seen previously in this bootcamp, there are many libraries and tools that allow us to run GPT models in our own devices.

We've experimented with the Hugging Face's `transformers` library, and we could run many models using tools like `pyTorch` and `TensorFlow`.

Configuring these tools and models to work inside scripts is not always trivial or straightforward, and it can be a bit overwhelming for beginners.

On top of that, there are many other concerns like handling server connections, managing model parameters, dealing with caches and storage, fine tuning and prompting parsing that require coding and implementation before we can actually consume the models for tasks inside our applications.

We are going to see a developer tool that can help dealing with many of these concerns while paving an easier way for us to explore and use GPT models in our own devices.

* [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) repository
* Features
  * Manage, load and run models
  * Run text-to-text tasks in loaded models
    * Use Chat, Instructions and Notebook interfaces
    * Use chat templates
  * Configure the model parameters to get the best performance and compatibility in your hardware
    * Load models with CPU, GPU, VRAM and RAM limits, quantization and many other helpful configurations
  * Manage extensions
    * Text-to-speech and speech-to-text integrations
    * Image generation and computer vision
    * Translations
    * Multimodal pipelines and job handling
    * RAG and custom datasets
    * Downloading and managing AI Characters
    * Using vector databases
    * Building your own extensions
  * Run a local API
  * Fine tune models
* Preparing for installation
  * Following the [Official Instructions](https://github.com/oobabooga/text-generation-webui?tab=readme-ov-file#how-to-install) should work for most cases
  * Depending on your Operating System and your Hardware, you may need to install some dependencies and configure your environment
  * Not all CPUs and GPUs are compatible with all models and configurations
    * NVidia on Linux and Windows currently has the best compatibility (as of March 2024)
    * AMD GPUs on Linux and Windows may work fine with some small configurations or adjustments
    * Apple and Intel chips may require some heavy workarounds and adjustments, or sometimes may not work at all
* Installation steps
  * Clone the repository
  * Run the installation script
    * Use `start_linux.sh` for Linux
    * Use `start_windows.bat` for Windows
    * Use `start_macos.sh` for MacOS
    * Use `start_wsl.bat` for Windows Subsystem for Linux
  * Wait for the download and installation of dependencies to finish
  * When prompted, select your GPU manufacturer and model
  * Confirm selection and wait until the entire installation process finishes
  * Open your browser and go to <http://localhost:7860> to test if the application is working
* Alternatives
  * Using a [Docker container](https://github.com/oobabooga/text-generation-webui/wiki/09-%E2%80%90-Docker)
  * Using a [Google Colab notebook](https://github.com/oobabooga/text-generation-webui?tab=readme-ov-file#google-colab-notebook)

## Using Text Generation WebUI

We are going to use the Text Generation WebUI tool to run Generative AI tasks in our own devices using many different models and configurations.

* Practical exercises
  * Exercise 3: Learning how to use the [Text Generation WebUI](./project/02-Text-Generation-WebUI.md)
  * Exercise 4: [Downloading and running a GPT model](./project/03-Running-GPT-Model.md)
  * Exercise 5: [Using chat completion](./project/04-Chat-Completion.md)

## Next steps

* Using the Text Generation WebUI
* Loading and running models
* Text Generation WebUI extensions
* Running a local API
