# Lesson 09: Deep Dive on GPTs

In this lesson we'll dive into some of the technical details behind loading GPTs and how the inference process works. We'll experiment with many different parameters that can increase the performance and compatibility of models depending on the hardware we're using, and we'll evaluate how different models behave in these configurations.

We will experiment and learn about many different models types and the major differences between them in terms of precision, performance and hardware requirements.

We're going to study more about the training process of GPTs, and how models can be enhanced with datasets and LoRAs to perform better at certain tasks.

To consolidate our learning on how GPTs work, we'll experiment with fine-tuning a simple GPT-2 model to generate text based on the information present in a local dataset.

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
* Install and run [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui?tab=readme-ov-file#how-to-install) in your device
* Install the latest [TensorFlow](https://www.tensorflow.org/install) (version 2.5.1 or above) in your environment

## Review of Lesson 08

* Weekend project
* Interacting with local models
* Replacing OpenAI with local API services in applications
* Testing prompts to improve the quality and precision of generation
* Building an AI application

## Running GPT models

* Model loaders
  * Hardware requirements
  * Model types
    * Full precision
    * GPTQ
    * GGUF (and GGML)
    * EXL2
    * AWQ
    * Others
  * Hardware requirements and tweaks
    * GPUs
    * Using consumer grade GPUs
    * CPUs
    * Using GPU VRAM
    * Using CPU RAM
* Tweaking GPT model to run in your hardware
  * Quantization
  * CPU Offloading
  * GPU VRAM usage limits
  * CPU RAM usage limits
  * Using disk cache
  * Context extension
  * Splitting workloads for multiple GPUs
  * Handling sequence lengths
  * Handling layers
  * Using batches
* Using LoRAs

## Overview of GPT training

* Training
  * Architecture
  * Hardware requirements
* Datasets
  * Formats
  * Data structure
  * Using raw text datasets
  * Using json objects
  * Considerations about dataset size and variety
  * Considerations about dataset quality and data cleaning
* Training jobs
  * Iterations
  * Convergence
  * Measuring and managing loss

## Experimenting with GPT-2

* What is [GPT-2](https://openai.com/research/better-language-models)
* Using GPT-2 for training
  * Using [GPT-2 Simple](https://github.com/minimaxir/gpt-2-simple) package
* Parameters size
* Text dataset
* Token limits

## Fine-tuning GPT-2

* Practical exercises
  * Exercise 1: [Train GPT-2 Small](./project/00-Train-GPT2-Small.md) to generate text with a dataset of food recipes
  * Exercise 2: [Train GPT-2 Medium](./project/01-Train-GPT2-Medium.md) to generate text with a dataset of movie scripts

## Next steps

* Overcoming the limitations of GPTs
* Understanding what a GPT assistant is
* Building and testing an Assistant with OpenAI APIs
* Exploring Retrieval-Augmented Generation (RAG)
