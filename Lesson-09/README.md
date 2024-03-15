# Lesson 09: Deep Dive on GPTs

TODO

## Pre-requisites

TODO

## Review of Lesson 08

* Weekend project
* Building applications using local AI services
* Testing prompts to improve the quality and precision of generation
* Building a storytelling application

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
