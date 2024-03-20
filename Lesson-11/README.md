# Lesson 11: Exploring More AI Models

In this lesson we will dive deeper into the realm of AI models, exploring a variety of text generation, code generation, and image generation models. We will compare different models such as GPT, Llama, Claude, Mistral, and Gemma to understand their strengths and weaknesses in generating text.

We will overview the image generation techniques involving multi-modal models, neural network-based models, and transformers-based models, understanding their advantages and applications.

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
* Create an account with [Vercel](https://vercel.com/) to use the [Vercel AI Playground](https://sdk.vercel.ai/)
* Create an account to use [ChatGPT](https://chat.openai.com/)
* Create an account to use [Bing Image Creator](https://www.bing.com/images/create)

## Review of Lesson 10

* GPT Assistants
* Assistant with OpenAI APIs
* Limitations of GPTs and ways to overcome them
* Retrieval-Augmented Generation (RAG)

## Comparing Text Generation Models

* The [Vercel AI Playground](https://sdk.vercel.ai/)
* Comparing using prompts
* Different versions of OpenAI GPT
* Different versions of [Llama](https://llama.meta.com/)
* Testing [Claude](https://claude.ai/)
* Testing [Mistral](https://mistral.ai/)
* Testing [Gemma](https://blog.google/technology/developers/gemma-open-models/)

### Comparing Text Generation Quality

* Practical exercise
  * Exercise 1: [Using Vercel AI Playground](./project/00-Using-Vercel-AI-Playground.md) to compare different text generation models

## Code Generation Models

* Training and fine-tuning for code
* Instructions
* Retrieval and context evaluation techniques
* Tweaking behavior with specific parameter ranges and constraints

### Code Generation Examples

* [CodeLlama](https://ai.meta.com/blog/code-llama-large-language-model-coding/)
* [Copilot](https://copilot.github.com/)
* [GhostWriter](https://replit.com/ai)
* [CodeWhisperer](https://aws.amazon.com/codewhisperer/)
* [Cody](https://sourcegraph.com/docs)
* [Devin](https://www.cognition-labs.com/blog), the "AI software engineer"

## Image Generation Models

* What are multi-modal models
* Multi-modal models vs single-modal models for image generation
* Generative AI for images

### Image Generation Examples

* [DALL·E-2 and DALL·E-3](https://labs.openai.com/) with [ChatGPT](https://chat.openai.com/)
* [DALL·E-3](https://labs.openai.com/) with [Designer](https://www.bing.com/images/create) (formerly known as Bing Image Creator)
* [Midjourney](https://www.midjourney.com/showcase)
* [DreamStudio](https://beta.dreamstudio.ai/generate)
* [Image-FX](https://aitestkitchen.withgoogle.com/tools/image-fx)

### Comparing Image Generation Quality

* Practical exercise
  * Exercise 2: [Generate Images with ChatGPT and Bing](./project/01-Generate-Images.md) to compare outputs

### Overview of Image Generation Techniques

* Multi-modal approach
  * AI applications like ChatGPT are enabled to consume and generate data in multiple formats, like text, image, video and audio (so called multi-modal AIs)
  * DALL·E is a variant of the GPT-3 transformer model developed by OpenAI that leverages the concept of unsupervised learning where the model learns to generate images from text descriptions
    * DALL·E uses a technique called "transformer language models" to generate images from text descriptions, by learning the relationship between the two from a large dataset
* Neural Network based Models
  * The same way that Neural Networks can be used to process text outputs based on their training data, they can be used to build image generation models
  * Some examples are the use of Generative Adversarial Networks (`GANs`), Variational Autoencoders (`VAEs`), Convolutional Neural Networks (`CNNs`) and Recurrent Neural Networks (`RNNs`)
* Transformers based models
  * Similar to what we saw with Text Generation GPTs, the Transformers architecture can be used to generate images from text descriptions, mapping the relationship between the tokens in the prompt to the images being generated
  * The Transformer model uses self-attention mechanisms to weigh the importance of different parts of the input data, allowing it to capture complex dependencies and generate high-quality images
  * Transformer-based models have several advantages over traditional neural network architectures, including the ability to handle long-range dependencies, parallelize computation, and scale to large datasets
  * Because of that, they have achieved state-of-the-art results in image generation models

## Generating Images with Stable Diffusion

* Overview of Stable Diffusion
  * Stable diffusion is a type of generative model that uses a process called diffusion to model the generation of images
  * The basic idea is to iteratively apply a series of transformations to a random noise vector until it matches the target image
  * At each step, the transformation is chosen such that it moves the current state of the noise vector closer to the target image
* Running a Diffusion Model
  * The process of running a diffusion model involves iteratively applying a series of transformations to a random noise vector until it matches the target image
  * The transformations are chosen such that they move the current state of the noise vector closer to the target image
  * The process is repeated until the noise vector matches the target image
* Using Hugging Face's [Stable Diffusion Pipelines](https://huggingface.co/docs/diffusers/quicktour)
  * Hardware requirements
  * Dependencies
  * Installation
  * Usage

### Using Diffusion Models with Python

* Practical exercise
  * Exercise 3: [Generate Images with Stable Diffusion](./project/02-Generate-Images-Diffusion.md)
    * Code and run [Diffusion.py](./project/Diffusion.py) to generate an image from a text prompt

## Next Steps

* Generating images with AI
* Image generation models
* Stable diffusion overview
* OpenAI Image Generation APIs
