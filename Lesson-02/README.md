# Lesson 02: Introduction to Machine Learning, Transformers and LLMs

In this lesson, we will introduce the basic concepts of machine learning, transformers and GPTs to better understand how Generative AI works, their capabilities and limitations.

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

## Review of Lesson 01

* What is AI
* Capabilities and limitations
* Practical uses of AI
* Using AI for text-to-text tasks
* Does ChatGPT sounds like a person?
* Is ChatGPT intelligent?

## Introduction to Machine learning

* How can a computer _learn_?
* [Machine learning](https://en.wikipedia.org/wiki/Machine_learning) is a broad terminology for a set of algorithms that can learn from and/or make predictions on data
* There are many forms of Machine Learning
  * [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning) is the most common form of machine learning, which consists of learning a function that maps an input to an output based on example input-output pairs
    * It requires a _training dataset_ with input-output pairs
    * The algorithm learns from the dataset and is able to make/extrapolate predictions on new data
  * [Unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning) is a type of machine learning that looks for previously undetected patterns in a data set with no pre-existing labels
    * It requires a _training dataset_ with input data only
    * The algorithm learns from the dataset and is able to make predictions on new data
  * [Reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) is a type of machine learning that enables an agent to learn in an interactive environment by trial and error using feedback from its own actions and experiences
    * It requires a _training dataset_ with input data and feedback
    * The algorithm learns from the dataset and is able to make predictions on new data
  * There are many other models and techniques that can be applied/extended
    * Semi-supervised learning
    * Self-supervised learning
    * Multi-task learning
    * Transfer learning
    * Meta learning
    * Online learning
    * Active learning
    * Ensemble learning
    * And many others
* These models have been evolving and improving over the years, aiming to output some form of _intelligence_ from the data, mimicking human-like behavior
  * For example, some advanced Machine Learning algorithms are using [Neural Networks](https://en.wikipedia.org/wiki/Neural_network) to compute complex functions and make predictions on data in ways that a "normal" program would take billions or more of lines of code to do
* This _brain-like_ computational algorithms have been used to extend the powers of AI in exponential scales, much more than what _traditional_ computing could do
  * An example of that is [Deep Learning](https://en.wikipedia.org/wiki/Deep_learning), which is a subset of machine learning that uses _neural networks_ with many [layers](https://en.wikipedia.org/wiki/Artificial_neural_network#Deep_neural_networks) to learn from data and make much more complex predictions on it
  * Neural Networks like [CNNs](https://en.wikipedia.org/wiki/Convolutional_neural_network) and [RNNs](https://en.wikipedia.org/wiki/Recurrent_neural_network) have been used for powering many AI applications for things like image and text recognition and generation, computer vision, and many others
  * Currently (as of March 2024), the most advanced form of Deep Learning is the [Transformers](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) architecture, which is a type of neural network that has been used to power many AI applications, including the GPT models
    * Different from traditional neural networks, transformers are able to process data in parallel, which makes them much faster and more efficient than traditional neural networks
    * This simple technical detail, aligned with the right market/investment conditions in the last years, has made possible for the Generative AI boom that we are experiencing now (as 2024)
* To understand how transformers work, we will use samples from the [Hugging Face tutorials](https://huggingface.co/docs/transformers/index), that makes it simple and straightforward to start using these tools and techniques without the need to understand the deep technical details of the models beforehand

## Introduction to transformers

Instead of going through the deep technical details of transformers, we will use frameworks, tools and libraries that abstract away most of the complexities for the hard computational, mathematical and statistical work that is required to make these algorithms work.

In fact, we're going to use pre-made models and shortcuts that makes it as simple as just calling a function to execute tasks over data being passed as parameter.

>Note: It is of great importance to look after these concepts later on, so you know exactly what is happening under the hood. But for now, for the sake of building functional AI applications as quickly as possible, we will focus on the practical aspects of using these abstractions and simplifications.

* Machine Learning frameworks and tools
  * [TensorFlow](https://www.tensorflow.org/)
  * [PyTorch](https://pytorch.org/)
  * [JAX](https://jax.readthedocs.io/en/latest/index.html)
* Using a library to abstract away complexities
  * [Transformers](https://github.com/huggingface/transformers)
* Getting started with a simple python script
* Using `Pipelines`
  * Downloading models
  * Using sample data
* Using `Tokenizer` and `Model` shortcuts
* Working with sample `datasets`
* Following a tutorial for a _NLP_ pipeline

## Getting started with Transformers

Hugging Face's Transformers library can abstract most of the complexities of using Machine Learning and other AI techniques, making it simple to use and apply these models to real-world problems.

The only concepts you need to fully understand when interacting with this library are: the _configuration_ itself, the _model_ that you are using, and the required _processor_ for the task you are trying to accomplish.

* Using [Transformers](https://github.com/huggingface/transformers) Library from Hugging Face
* Using the [Pipelines](https://huggingface.co/docs/transformers/main_classes/pipelines) API for running pre-trained tasks
  * Running these tasks requires almost no previous knowledge in AI or Machine Learning or even programming at all, thanks to the Hugging Face's [Philosophy](https://huggingface.co/docs/transformers/main/en/philosophy)
* Generating text by running LLMs with [Generate](https://huggingface.co/docs/transformers/main/en/model_doc/phi#transformers.PhiForCausalLM.generate) API
  * [Text generation with LLMs](https://huggingface.co/docs/transformers/main/en/llm_tutorial#generation-with-llms) make use of _Autoregressive generation_ to iteratively infer outputs from a given input from a model
* Practical exercises
  * Exercise 1: [Installing Hugging Face's Transformers](./project/00-Install-Transformers.md)
  * Exercise 2: [Using a Sentiment Analysis pipeline](./project/01-Sentiment-Analysis-Example.md)
    * Code and run [SentimentAnalysisExampleV0.py](./project/SentimentAnalysisExampleV0.py) and [SentimentAnalysisExampleV1.py](./project/SentimentAnalysisExampleV1.py) in this exercise
    * More examples on [Transformers quick tour](https://huggingface.co/docs/transformers/quicktour)
  * Exercise 3: [Using a Text Generation pipeline](./project/02-Text-Generation.md)
    * Code and run [TextGeneration.py](./project/TextGeneration.py) in this exercise

## Next steps

* Getting to know GPTs
* Using OpenAI APIs for running GPTs for text-to-text tasks
