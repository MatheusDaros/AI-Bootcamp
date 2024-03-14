# Lesson 03: Introduction to GPTs

In this lesson, we will advance to the introduction of GPTs, the Generative Pre-trained Transformers, and how they work.

We will have a better overview on how transformers are used to train and compute outputs from models, and we will evaluate in depth the capabilities and limitations of current GPT applications.

We will exercise more on using the Hugging Face's Transformers library to run pre-trained models for text-to-text tasks with a LLM, but this time using sampling methods and tweaking the model configurations to understand more on the maths and logics behind the models.

We will also use the OpenAI APIs to run GPTs for text-to-text tasks, by invoking a remote execution of a server that runs the GPTs for us.

For this lesson, you should have a basic understanding on how to use developer tools in your device. You should also have at least a very basic understanding of the python programming language syntax. You should set up an account in the OpenAI Platform, and have at least 5 USD credits in your account to run the API commands in the OpenAI exercise.

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

## Review of Lesson 02

* What is Machine Learning
* What are Transformers
* Practical uses of Transformers
* Using Transformers for text-to-text tasks with Hugging Face's Transformers library
* What are LLMs
* Using pre-trained LLMs for text generation
* Running a LLM inference for text generation with Hugging Face's Transformers library
* What is a _pre-trained_ model?
* What are these _tokens_ and what is _encoding_/_decoding_?
* What is a _prompt_?
* What is _inference_?

## Introduction to GPTs

* GPTs (Generative Pre-trained Transformers) are a type of LLMs (Large Language Models) that are trained to generate _outputs_ (inference) from _inputs_ (prompts) based on their _training data_ (pre-training)
* Even though GPTs are able to follow some sort of _intelligent instructions_, like chatting, answering questions, generating stories, completing code and such, they are not _intelligent_ in the sense of _understanding_ the _meaning_ of the _inputs_ and _outputs_ they're dealing with
  * GPTs don't actually _understand_ the _inputs_ and _outputs_ they're dealing with, they just learn from the training data (using `Machine Learning`) how to generate outputs from inputs based on _patterns_ and _probabilities_ observed in the training data
  * GPTs don't remember things that they process after the training phase, they just _forget_ the _inputs_ and _outputs_ they're dealing with after they're over with it
    * GPTs can store the chat history in `context` while processing tasks, but this is only a temporary storage for the current chat/inference session being run
    * When the chat/inference session is deleted, the `context` is lost and the GPT _forgets_ everything it processed
  * GPTs don't _learn_ or _improve_ after the training phase, no matter how many times they process similar _inputs_ and _outputs_
    * GPTs can be _fine-tuned_ to process specific _inputs_ and _outputs_ after the training phase, but this is a different process from the training phase and it's not a _learning_ process, it's just a _tweaking_ process

### Applications using GPTs

Some examples of applications using GPTs:

* [ChatGPT](https://chat.openai.com/)
* [Google Gemini](https://gemini.google.com/) (formerly known as Bard)
* [Bing AI](https://www.bing.com/chat) (also known as Copilot)
* [Claude AI Chat](https://claude.ai/chats)
* [Pi](https://pi.ai/talk)
* [Grok](https://grok.x.ai/)

All of these applications use many different techniques and models to process many _modalities_ of tasks, but all of them incur in the same limitations and capabilities of GPTs, in different degrees and manifestations.

There are many discussions about evolving these applications for reaching [AGI](https://en.wikipedia.org/wiki/Artificial_general_intelligence) (Artificial General Intelligence) capabilities using GPTs and similar models. As far as it seems (by early 2024), this is a very complex and long-term goal that is not yet feasible with the current state of the art in AI and Machine Learning (or might never be at all).

### How GPTs works

* Model training
  * GPTs are pre-trained models (hence the name) that are trained in large and diverse dataset of texts for computing _patterns_ and _probabilities_ between the contents present in the training data
    * For example, a model trained in terabytes of chemical and biological texts may be able to generate correlations between chemical components names and illness symptoms with much more _accuracy_ and _reliability_ than a model trained in terabytes of literature and poetry texts (probably)
    * Usually, the more data and the more diverse the data, the better the model will be able to generate outputs based on the _patterns_ and _probabilities_ observed in the training data
    * Current state-of-the-art models are trained in datasets with hundreds of terabytes of texts and other contents, and the training process can take weeks or even months to be completed
  * The process of training these models involves the use of `Machine Learning` techniques, like we studied in the previous lesson
* Tokens encoding and decoding
  * All of the calculations of these models are not over the character strings themselves in _raw_ form, but rather over _tokens_ that are _encoded_ and _decoded_ from these character strings
  * Each word (or fragment of letters) is broken down into tiny pieces ([n-grams](https://en.wikipedia.org/wiki/N-gram)) that are used to compute the _patterns_ and _probabilities_ between the contents present in the training data
  * The _encoding_ process is the process of converting the character strings into these _tokens_, and the _decoding_ process is the process of converting these _tokens_ back into the character strings
* Transformers
  * The process of relating the tokens to each other in the training data is done by these [Transformers](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) neural networks that we saw in the previou lesson
  * These transformers are used both in the training phase and in the inference phase of these models to calculate the relations between the tokens and generate the outputs based on these
* Inference
  * The process of generating outputs from inputs in a transformer is called inference, and can be accomplished much more quickly for `prompting` than the training phase, since the _patterns_ and _probabilities_ between the contents present in the training data are already computed and stored in the model
  * For every `prompt` provided, the model calculates the most probable `output` based on the model data
  * Since the model doesn't understand the concepts of _correct_ or _incorrect_, _meaningful_ or _nonsensical_, _helpful_ or _toxic_, it up to the person or system passing the `prompt` to the model to _judge_ the `output` generated by the model by their own criteria and standards
* Prompting
  * After the model has been trained, it won't execute anything else on its own, unless it's _prompted_ to do so
  * The `prompt` being passed to the model may vary a lot in format, depending on the task being executed and the model configurations
    * For example, a `prompt` for a chatbot may be a question like "_what is your name?_", while a `prompt` for a code generator may be a code snippet like "_for i in range(10): print(i)_"
    * Most models have certain _structures_ for prompts, allowing for multiple _actors_ to interact inside the model, usually with a "system" actor for answering things that an "user" actor requests from it
  * The `prompt` is the input that the model will process to generate the output, and it can be as simple as a single word or as complex as a full book
  * The `prompt` is the most important part of the process of generating outputs from inputs, and it can be _engineered_ in many different ways to _guide_ the model to generate more _meaningful_ outputs
* Context
  * GPTs have use limited _context_ maximum length for processing `prompts`, and they can store the chat history in `context` while processing tasks, but this is only a temporary storage for the current chat/inference session being run
  * When passing too much data in a `prompt`, the model may not be able to process it all correctly, and may even disregard some parts of the `prompt` or of the `training data` based on the model configurations and parameters
  * The context size usually range from a few hundreds to a few thousands of tokens, with some exceptions to up to one million tokens context size
    * This means that the more information you include in the `prompt`, the less _token space_ the model will have to evaluate the trained data against what is being asked
* Fine tuning
  * If the GPTs trained in random internet text were not adjusted, they would merely regurgitate random internet texts, giving responses completely irrelevant, inaccurate, or even nonsensical.
  * To save space in the `context` while tweaking the accuracy of the outputs, the `fine tuning` process can be used to _guide_ the model to generate more _meaningful_ outputs
  * In the `fine tuning` process, the model is trained to prioritize reliable sources and accurate information, reducing the likelihood of generating answers based on misinformation or low-quality internet texts
  * These processes often includes incorporating human feedback to correct errors and biases in the model's responses. This iterative process helps in aligning the model's outputs with human values and expectations
  * Another common practice is to apply targeted training, that involves fine-tuning the model on a specific dataset that is relevant to the desired application
    * This targeted approach helps the model learn context and nuances pertinent to particular topics or industries.
* RAG
  * The `RAG` (Retrieval-Augmented Generation) process is a technique that combines a language model's generative abilities with an external information retrieval system
  * Instead of passing all the context for a question in the prompt, the RAG first identifies relevant information from a large database, then incorporates this data into the language model's query
  * This method significantly expands the model's precision and accuracy, particularly for queries requiring specific information
  * This is more efficient than passing all the information in the prompt, and also is much simpler than fine-tuning the model with the new data

### Limitations of GPTs

To better understand the capabilities of GPTs, let's highlight some of the most impactful implications of their limitations:

* Lack of understanding
  * Questions like "_who are you_" and "_what is your name_" are not understood by GPTs, they just generate outputs based on patterns and probabilities observed in the training data
  * If the training data contains texts like "_I am a chatbot_" and "_My name is ChatGPT_" frequently associated with these questions, the GPT will generate outputs like "_I am a chatbot_" and "_My name is ChatGPT_" when asked
  * If the training data is some amount of text where these questions are frequently associated with other words and phrases, the GPT will generate outputs based on these associations
    * For example, a GPT trained in the Don Quixote book might generate outputs like "_I am Don Quixote_" and "_My name is Alonso Quijano_" when asked these questions
  * There are some techniques like `Fine Tuning`, `HFRL` (Human Feedback Reinforcement Learning), `Prompt Engineering`, `RAG` (Retrieval-Augmented Generation)  and `Control Codes` that can be used to _guide_ the GPTs to generate more probably _meaningful_ outputs, but these are not _learning_ processes, they are just _tweaking_ processes
  * Ultimately, there's no current technique that can make a GPT to actually _understand_ and _reason_ about the _inputs_ and _outputs_ they're dealing with, like a human mind would do
* Sensitivity to input
  * GPTs are very sensitive to the _inputs_ they're dealing with, and they can generate very different _outputs_ based on very small changes in the inputs _phrasing_ (or `prompting`)
  * Asking the same question in different word orders, or even using different languages, can lead to very different outputs, some times even conflicting or entirely unrelated
    * For example, asking "_what is the capital of France_" and "_France's capital is_" can lead to very different outputs, depending on the model training
    * This happens because even if the `semantic` meaning of these questions are almost the same in these two phrasings, the `syntactic` meaning is different, and GPTs are very sensitive to these differences
    * In practice, every _character_ different in a `prompt` can move the coordinates in the _text space_ function that computes the output value over that input, regardless if that character changes or not the _semantic_ meaning of the `prompt`
      * As a loose metaphor, we could imagine a function `f(x)` that gives possibly very different outputs if we give `x = 1`, `x = 1.00000001` or `x = 1.000000000000...001`, even if the `semantic` meaning of these inputs are almost the same
* Inconsistency
  * GPTs sometimes may be very inconsistent in generating outputs for the same inputs, even if the _inputs_ are the same
  * Since most operations in the _inference_ process are based on _probabilities_ and _patterns_ observed in the training data, the _outputs_ can be very different for the same _inputs_ based on the _randomness_ of the _sampling_ process
  * The results can be more or less deterministic based on the model _configurations_ and _parameters_ used in the _inference_ process
    * There are some parameters like `Temperature`, `Top-K`, `Top-P` and `Nucleus Sampling` that can be used to _control_ the _randomness_ of the _sampling_ process
  * A model operating with _greedy search_ will generate the same outputs for the same input, while a model operating with _random sampling_ (or `temperature` sampling) might often generate different outputs for the same input
* Incorrect or Nonsensical Outputs (and hallucinations)
  * GPTs can generate incorrect or nonsensical outputs based on the _inputs_ they're dealing with, specially when the _inputs_ are very _ambiguous_ or _open-ended_
  * This is not necessarily a defect of the GPTs, but a consequence of the _patterns_ and _probabilities_ observed in the training data
    * For example, a GPT trained in the anatomy of humans may answer the question “How many eyes does a spider have?” with “Two” because it has learned from the training data that most subjects have two eyes, and it might not be clear in the training data that spiders are not humans
      * Even though this information is incorrect (according to the common sense definition of spiders), it might be _statistically_ correct to associate "number of eyes (of a living thing)" with "two" based on the training data of that model
  * This is very common to happen with ambiguous things, like person names, locations, historical events, dates, quantities and such subjects where you have many different _correct_ answers based on the _context_ of the _inputs_
    * The question "Who is James" may vary a lot depending on the _context_ of the question and also based in the training data of the model
      * For example, if the training data contains a lot of texts about James Bond, the GPT may answer "James Bond" to this question, even if the question is about another James
  * The term [Hallucination](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) is often used in AI to describe these incorrect or nonsensical outputs, because they are generated based on _patterns_ and _probabilities_ observed in the training data, not based on _understanding_ or _reasoning_ about the _inputs_ and _outputs_ they're dealing with
    * These hallucinations can be very dangerous, since the GPTs may provide very _convincing_ and _realistic_ outputs based on _patterns_ and _probabilities_ observed in the training data, even if these outputs are completely incorrect or nonsensical
* Bias and toxicity
  * GPTs can generate outputs that are biased and toxic based on the _inputs_ they're dealing with, specially when the information in the _training data_ are biased and toxic
  * Techniques like `Fine Tuning` and `HFRL` can help to mitigate this effect by tweaking the responses to be as _helpful_, _harmless_ and _honest_ as possible
    * But also consider that even human feedback and direct overseeing of the training data can't guarantee that the GPTs will generate outputs that are not biased and toxic, since the very terms of _helpfulness_, _harmlessness_ and _honesty_ can be very subjective, depending on many social, cultural, contextual and personal factors
* No (native) access to Real-Time information
  * Since GPTs don't _learn_ or _improve_ after the training phase, they can't access any information that happen after their training, unless explicitly _fed_ with this information in the _inputs_ or with some technique like `RAG` (Retrieval-Augmented Generation) or similar
  * This means that GPTs can't provide real-time information about anything at all, like news, events, weather, stock prices, sports results, and such
    * It is certainly possible to _feed_ GPTs with real-time information, but this is a different process from the training phase and it's not a _learning_ process, it's just passing data to it with hope that it will give it back to you correctly

### Use cases of GPTs

Some examples of practical tasks that GPTs can accomplish with these forementioned applications:

* Writing
  * Articles
  * Stories
  * Code
  * Social media posts
  * Emails
  * Documentation
* Reading
  * Summarization
  * Alerts
  * Filtering
  * Translation
  * Categorization
  * Ranking
* Chat
  * Customer support
  * Personal assistants
  * Chatbots
  * Social media
  * Forums
  * Messaging
  * Sales
  * Interviews
  * Teaching
* Image recognition
  * Captioning
  * Tagging
  * Filtering
  * Categorization
  * Ranking
* Image generation
  * Art
  * Design
  * Animation
  * Editing
  * Rendering
  * Simulation
  * Videos
  * 3D models
* Tools and extensions

### Practical exercises with GPTs

We can use the Transformers Text Generation Pipeline to run GPTs for text-to-text tasks, just like we have done at Lesson 2.

These same tasks can be accomplished using OpenAI APIs, by invoking a remote execution of a server that runs the GPTs for us.

* Practical exercises
  * Exercise 1: [Using a Text Generation pipeline](./project/00-GPT-Text-Generation.md) to run a GPT for text generation
    * Code and run [TextGenerationExtended.py](./project/TextGenerationExtended.py) in this exercise
  * Exercise 2: [Using a Text Completion API from OpenAI](./project/01-OpenAI-Text-Completion.md) to run a GPT for text completion
    * Code and run [OpenAITextCompletion.py](./project/OpenAITextCompletion.py) in this exercise

## Next steps

* OpenAI APIs
* Handling requests
* Streaming responses
* Using the OpenAI Playground
* Model configurations
* Models comparison
* Prompt engineering
* Weekend project
