# Lesson 09: Deep Dive on GPTs

In this lesson we'll dive into some of the technical details behind loading GPTs and how the inference process works. We'll experiment with many different parameters that can increase the performance and compatibility of models depending on the hardware we're using, and we'll evaluate how different models behave in these configurations.

We will experiment and learn about many different model types and the major differences between them in terms of precision, performance and hardware requirements.

We're going to study more about the training process of GPTs, and how models can be enhanced with datasets and LoRAs to perform better at certain tasks.

To consolidate our learning about how GPTs work, we'll experiment with fine-tuning a simple GPT-2 model to generate text based on the information present in a local dataset.

## Prerequisites

* Learn how to use the shell/terminal/console/bash on your device
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
* Install and run [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui?tab=readme-ov-file#how-to-install) on your device
* Create an account at [Google Colab](https://colab.research.google.com)

## Review of Lesson 08

* Weekend project
* Interacting with local models
* Replacing OpenAI with local API services in applications
* Testing prompts to improve the quality and precision of generation
* Building an AI application

## Running GPT Models

Text Generation WebUI supports different model loaders, which enable loading various types of pre-trained GPT models, each with its own characteristics and requirements. We'll explore the most common model loaders and how they can be used to run GPT models on different hardware configurations.

* Model loaders
  * Hugging Face`s [Transformers](https://github.com/huggingface/transformers) Library
    * Loads full precision (16-bit or 32-bit) models
      * Models that usually have a clean name without terms like `GGUF`, `EXL2`, `GPTQ`, or `AWQ` in their names
      * Usually the model files are named `pytorch_model.bin` or `model.safetensors`
    * Full precision models use a ton of VRAM, so you will usually want to select the `load_in_4bit` and `use_double_quant` options to load the model in 4-bit precision using `bitsandbytes` if supported in your system
    * This loader can also load GPTQ models and train LoRAs with them, if configured correctly
  * [LLaMA.cpp](https://github.com/ggerganov/llama.cpp) Library using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) and [CTransformers](https://github.com/marella/ctransformers)
    * Loads `GGUF` models
  * [ExLlamaV2](https://github.com/turboderp/exllamav2)
    * Loads `GPTQ` and `EXL2` models
  * [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) and [GPTQ-for-LLaMA](https://github.com/qwopqwop200/GPTQ-for-LLaMa)
    * Loads `GPTQ` models
  * [AutoAWQ](https://github.com/casper-hansen/AutoAWQ)
    * Loads `AWQ` models
* Model types
  * Full precision
    * These models use the original 32-bit floating-point precision, offering the highest accuracy but requiring more memory and computational resources
    * These models are ideal for training and fine-tuning
  * GPTQ
    * GPT Quantized models use fewer bit widths (e.g., 8-bit or 4-bit) to represent the weights, reducing memory usage and computational requirements at the cost of some accuracy
    * These models are ideal for inference in low-resource environments, like using consumer-grade GPUs or even CPUs only
  * GGUF (and GGML)
    * GGML (GPT-Generated Model Language) is a tensor library designed for machine learning that uses `.ggml` files to store models
    * It was succeeded in August 2023 by the GGUF (GPT-Generated Unified Format) library, which uses `.gguf` files to store models
    * GGUF files can store both full precision and quantized models
    * A GGUF file has all the necessary metadata included in the model file, eliminating the need for additional files such as `tokenizer_config.json` that some other models require
  * EXL2
    * EXL2 (ExLlamaV2) is a model format with optimized compression
    * It is based on the same optimization method as GPTQ, but it allows for mixing quantization levels within a model to achieve any average bitrate between 2 and 8 bits per weight
    * These models are optimized for lower latency, and can use more of the available computational resources to speed up inference and training processes
  * AWQ
    * AWQ (Adaptive Weight Quantization) is a quantization technique that adaptively quantizes the model weights based on their importance, striking a balance between accuracy and efficiency
    * Similar to the EXL2 format, AWQ models can yeld great performances if given enough computational resources
* Configuration tweaks
  * GPUs
    * Many models are optimized for making use of GPU clusters for running inference and training
    * GPUs are especially effective for processing GPTs because they can handle the large matrix multiplications required by the models much better than CPUs
    * The amount of VRAM available on the GPU is a major factor in determining the size of the model that can be loaded and the amount of data that can be processed at once
  * Using consumer grade GPUs
    * Consumer-grade GPUs are usually less powerful than professional-grade GPUs, but they can still be used to run GPT models
    * GPTQ models are especially well-suited for running on consumer-grade GPUs because they require less memory and computational resources
  * Configuring models to run in consumer-grade GPUs
    * Some loaders like `Transformers` and `GPTQ-for-LLaMa` may allow you to configure the model to offload some of the computation to the CPU, reducing the amount of VRAM required on the GPU, but also greatly slowing down the performance of the models
    * The `llama.cpp` loader uses CPU only by default, so to make use of your GPU you will need to configure the loader to use the GPU by setting the `n-gpu-layers` parameter to a value greater than 0
    * Using quantization can also help reduce the amount of VRAM required to run the model on a consumer-grade GPU
  * CPUs
    * If you don't have access to a GPU, you can still run GPT models on a CPU preferably using `GGUF` models loaded with `llama.cpp` or `CTransformers`
    * Quantized models like `GPTQ` and `GGUF` with low bit widths are especially well-suited due to lower memory and computational requirements
      * When using `GPTQ` you can also choose a model that was quantized with a higher `groupsize` parameter, like `1024` (the default, more lightweight), `128` (more balanced) or `32` or less (more accurate but also heavier)
* Tweaking GPT model to run on your hardware
  * Quantization
    * Quantization is a technique that reduces the precision of the weights in a model, reducing the amount of memory and computational resources required to run the model
    * The trade-off is that quantized models are less accurate than full precision models
    * You can experiment with different bit widths to find the right balance between accuracy and efficiency for your use case
  * CPU Offloading
    * Some loaders allow you to offload some of the computation to the CPU, reducing the amount of VRAM required on the GPU
    * This can be useful if you have a consumer-grade GPU with limited VRAM
    * The trade-off is that offloading computation to the CPU will greatly slow down the performance of the model
  * Disk offloading
    * Some loaders allow you to offload some of the computation to the disk, reducing the amount of VRAM required on the GPU and CPU
    * This can be useful if you have a consumer-grade GPU with limited VRAM or even no GPU at all
    * The trade-off is that offloading computation to the disk is many times slower than offloading to the CPU, and should be used only as a last resort
  * GPU VRAM usage limits
    * Some loaders allow you to set a limit on the amount of VRAM that the model can use on the GPU
    * This can be useful if you have a consumer-grade GPU with limited VRAM
    * When the model exceeds the VRAM limit, the loader will automatically offload some of the computation to the CPU if configured to do so
      * Otherwise, the model will crash with an out-of-memory error
  * CPU RAM usage limits
    * It's also possible to set a limit on the amount of RAM that the model can use on the CPU
    * If both the GPU and CPU limits are set, the model will crash if it exceeds either limit
      * Some models allow caching to disk to avoid this, but this process is not very well supported and can lead to many errors and crashes
  * Using disk cache
    * As a last resort, you can use disk cache to store intermediate results and reduce the amount of memory required to run the models
    * Not all loaders support this feature, and it can be very slow and error-prone
  * Context extension
    * This technique allows you to run models with larger context sizes by splitting the input into smaller chunks and processing them separately
  * Splitting workloads for multiple GPUs
    * If you have multiple GPUs, you can split the workload between them for faster processing
    * This is very dependent on the loader and the model, and may require some manual configuration to work correctly on your system
    * Running GPTs in big clusters usually is done completely differently than this "artisanal" approach we're doing in this bootcamp, with proper load balancing and distribution of the workload and better orchestration of the GPUs by the model runner
  * Handling sequence lengths
    * Some models have a fixed sequence length that they can process, and will crash if the input is longer than this length
    * Some loaders allow for limiting the sequence length to avoid this issue
    * You can experiment with different sequence lengths to find the right balance between accuracy and efficiency for your use case
  * Handling layers
    * Many loaders allow you to configure how the models layers are handled during inference, providing a trade-off between accuracy and efficiency between using GPUs and CPUs to process outputs
    * If you have a GPU available in your system, you can experiment with loading all the layers on the GPU to speed up the processing and achieve better quality outputs
      * If you reach an "Out of Memory" error, you can try to gradually increase the number of layers loaded on the CPU until the model loads successfully
  * Using batches
    * Some loaders allow you to configure the batch size of the model, which can greatly affect the performance of the model
    * Larger batch sizes can speed up the processing of the model, but may require more memory and computational resources
    * Smaller batch sizes can reduce the memory and computational requirements of the model, but may slow down the processing
    * If you're having "Out of Memory" errors, try reducing the batch size to the minimum (one sequence at a time) and see if the model runs
* Using LoRAs
  * LoRAs (Low-Rank Adaptation) are a technique for fine-tuning large language models with minimal additional memory requirements
  * The idea behind LoRA is to adapt a model to a specific task without having to fine-tune all the parameters within the model, which can be very memory-intensive and computationally expensive
    * A LoRA can modify the weights of the pre-trained model in a low-rank subspace, rather than updating all its parameters
    * It's a form of parameter-efficient transfer learning, which is a research area focused on adapting pre-trained models to new tasks with minimal changes to the original model
  * The low-rank matrices are used to modify the behavior of the attention and feed-forward layers within the transformer model
  * Currently (as of March 2024) the `llama.cpp`, `ctransformers` and `AutoAWQ` loaders support loading LoRAs

## Overview of GPT Training

* Training
  * Architecture
    * The architecture of GPT is based on the transformer model, which is characterized by self-attention mechanisms that weigh the importance of different parts of the input data to try to better _understand_ the context of words in a sentence
    * The architecture typically includes several layers of transformer blocks, each containing multi-head self-attention and feed-forward neural networks
      * For this, the model needs to be **trained** to predict the next word in a sentence, given the previous words
    * The GPT models are often pre-trained on a large corpus of text data and then fine-tuned for specific tasks
  * Hardware requirements
    * Training GPT models is resource-intensive and requires significant computing power
    * High-performance GPUs or TPUs are generally necessary to expedite the training process
    * As the model size increases (with more parameters), the hardware requirements scale up, often necessitating distributed training across multiple GPUs or TPUs to accommodate the computational load and memory requirements
* Datasets
  * Formats
    * Datasets for training GPT models can come in various formats, but they are typically in a text-based format that the model can easily process
    * This could be plain `TXT` files, `CSV` files with text data, or even more complex formats like `JSON` or `XML`
    * Some models are trained on specialized formats like TensorFlow's `TFRecord` format, which can be more efficient for large datasets
  * Data structure
    * The data structure of the dataset is important for effective training
    * The data should be structured in a way that allows the model to easily learn the relationships between words and sentences
    * This often means breaking the data up into manageable chunks, like sentences or paragraphs
  * Using raw text datasets
    * Raw text datasets can be used directly for training, but they may require some preprocessing to remove unnecessary characters or format the text in a way that the model can understand
    * The text be tokenized into a format that the model can process numerically, usually involving splitting the text into words or syllables and converting these into numerical tokens
  * Using `JSON` objects
    * JSON objects can be used to provide more structured data to the model
    * This could include additional metadata about each piece of text, or it could be used to provide more complex training examples, like conversations or question-answer pairs
    * When using JSON, the _training pipeline_ must parse the JSON structure to extract the relevant information for the model
  * Considerations about dataset size and variety
    * The size and variety of the dataset are important factors in training a GPT model
    * A larger dataset can help the model learn more about the relationships between words and sentences, leading to better performance
    * A diverse dataset can help the model generalize better to new data, improving its ability to generate coherent and relevant text
    * Bigger models can benefit from larger datasets, but smaller models must be trained with smaller and more focused datasets to produce good results
    * Curating the dataset to remove irrelevant, redundant, or low-quality data can improve the model's performance
    * For any given prompt, there's an ideal dataset size that will maximize the model's performance for that specific task
      * Adding more data beyond this point can actually decrease the model's performance for that specific task, while very probably it will also increase the model's performance for other tasks related to the data being added
      * Training a model with a dataset that is too small can lead to overfitting, where the model memorizes the training data rather than learning the underlying patterns
      * Adding too much data can lead to underfitting, where the model fails to learn the underlying patterns in the data and can't perform even in simple tasks related directly to the training data
  * Considerations about dataset quality and data cleaning
    * The quality of the dataset is crucial for training a GPT model
    * Every bit of data in the dataset ideally should be relevant to the task the model is being trained for
    * Some models are more sensitive to the quality of the data than others, and may require more careful curation of the dataset
      * For example, a model trained on a dataset of scientific papers may require more careful curation than a model trained on a dataset of movie scripts
      * There also some fine-tuning techniques that can help the model to learn better from the data to perform certain niche tasks
    * Data cleaning is an important step in preparing the dataset for training, but it can be time-consuming and labor-intensive since it often requires manual inspection and correction of the data
    * Automated tools can help with data cleaning, but they may not catch all errors or inconsistencies in the data
      * In some cases, the cleaning process can even **introduce** new errors or biases into the data, depending on the parameters being used to determine what is "clean" or "dirty" data
* Training jobs
  * A training job is a process of updating the model's parameters to minimize the difference between its predictions and the expected outputs
  * Iterations
    * An iteration, also known as an epoch, is a single pass (or cycle) through the entire training dataset during the training process
    * Each iteration, the model processes the data in small batches, updating its weights after each batch to minimize the error between its predictions and the actual outcomes (the next words in the text)
    * This process is repeated for many iterations until the model's performance stops improving significantly from one iteration to the next
    * During each iteration, the training data is typically divided into smaller batches to make the training process more computationally efficient
    * The size of the batch and the learning rate (how much the parameters are adjusted in each iteration) are important parameters that can affect the model's performance and training time
  * Convergence
    * Convergence in machine learning refers to the point in the training process where the model's performance stops improving significantly, and the model has learned the underlying patterns in the data
    * Essentially, convergence is an indicator of how much the model has learned from the training dataset, and how much further training is likely (or not) to yield substantial improvements
      * It's important to monitor for convergence within the training process, since after a certain point it can lead to overfitting, where the model becomes too specialized to the training data and performs poorly on new, unseen data
    * Convergence is typically monitored by tracking the model's _loss_ or accuracy on a validation set during training
    * To prevent overfitting, often the training processes implements an _Early Stopping Trigger_, where training is stopped when the model's performance on the validation set starts to degrade, even if the performance on the training set might still continue to improve
  * Measuring and managing loss
    * Loss is a measure of how well the model's predictions match the expected outputs
      * It quantifies the difference between the predicted and actual values
      * Different loss functions can be used depending on the task and the type of output
      * Common loss functions include mean squared error (MSE) for regression tasks and cross-entropy loss for classification tasks
    * A higher loss indicates that the model's predictions are further from the expected outputs, while a lower loss indicates that the model's predictions are closer to the expected outputs
    * If the model is being trained on a new dataset very different from the one it was pre-trained on, it's common to see a higher loss at the beginning of the training process
      * As the model learns the new patterns in the data, the loss should decrease over time
      * But if the loss parameter decreases too much (less than one), the model might start to "forget" the patterns it learned from the pre-training data and respond exclusively to the information present in the new data
    * During training, we keep track of the loss to gauge the model's performance cycle by cycle
      * The goal is to manage and reduce the loss with each iteration, until the model converges and the loss stabilizes near the desired value
      * This involves fine-tuning hyperparameters such as the learning rate, which controls how much the model's weights are adjusted during each update
      * If the loss is still far from the target but it stops to decrease, it's a sign that the model is not learning anymore and the training parameters should be fixed

## Experimenting with GPT-2

* What is [GPT-2](https://openai.com/research/better-language-models)
* Using GPT-2 for training
  * Using [GPT-2 Simple](https://github.com/minimaxir/gpt-2-simple) package
* Parameters size
* Text dataset
* Token limits

## Fine-tuning GPT-2

* Practical exercises
  * Exercise 1: [Train GPT-2 Small](./project/00-Train-GPT2-Small.md) to generate text with a text file dataset using a Google Colab instance
  * Exercise 2: [Train GPT-2 Medium](./project/01-Train-GPT2-Medium.md) to generate text with a text file dataset using the Text Generation WebUI [Training Tab](https://github.com/oobabooga/text-generation-webui/wiki/05-%E2%80%90-Training-Tab)

## Next Steps

* Overcoming the limitations of GPTs
* Understanding what a GPT assistant is
* Building and testing an Assistant with OpenAI APIs
* Exploring Retrieval-Augmented Generation (RAG)
