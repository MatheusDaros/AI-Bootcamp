# Lesson 06: Using GPT models in your own device

## Pre-requisites

TODO

## Review of Lesson 05

TODO

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
  * TODO: Explain the features listed in the github repository
* How to install
  * TODO: Explain how to install the tool
  * TODO: Explain the dependencies
* How to use
  * TODO: Explain how to use the tool - Interface - Main commands - Model selection - Model parameters - Model prompts - Model outputs - Extensions - Downloading models - Using the API flag

## Using Text Generation WebUI

We are going to use the Text Generation WebUI tool to run Generative AI tasks in our own devices using many different models and configurations.

* Practical exercises
  * Exercise 3: [Downloading and installing Text Generation WebUI](./project/02-Text-Generation-WebUI.md)
  * Exercise 4: [Downloading and running a GPT model](./project/03-Running-GPT-Model.md)
  * Exercise 5: [Using chat completion](./project/04-Chat-Completion.md)

## Next steps

TODO