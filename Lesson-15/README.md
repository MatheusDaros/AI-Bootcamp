# Lesson 15: AI Image Processing

In this lesson we're going to explore how diffusion models can be fine-tuned and enhanced using LoRAs and VAEs to greatly extend their image generation capabilities. We'll experiment with image datasets and techniques to properly correlate elements in an image to approximated text descriptions.

By the second half of this lesson we're going to explore more on the idea of extracting information from images, and we're going to learn about a technique called "Computer Vision" and how it can be used to process text from images.

We're going to see an overview on how the same versatile Transformers architecture we've previously discussed for text and image generation can be used again for image processing tasks. We're going to experiment using transformers to run Zero-shot detection and classification tasks to better understand what computer vision can do.

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
* Install [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) on your device and all the correct dependencies for your hardware
* Install [Dreambooth](https://github.com/d8ahazard/sd_dreambooth_extension) extension in Stable Diffusion WebUI and all the correct dependencies
* Download the [Full SD1.5 model](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors?download=true)
* Install the [Transformers](https://huggingface.co/docs/transformers/main/en/installation) library on your environment
* Install [Vision Process WebUI](https://github.com/isLinXu/vision-process-webui) on your device and all the correct dependencies for your hardware

## Review of Lesson 14

* Prompt engineering for image generation
* Configuring Stable Diffusion WebUI
* Capabilities and limitations of stable diffusion models
* Using ControlNet to guide the diffusion process
* ControlNet extension for Stable Diffusion WebUI

## Fine-Tuning Models with Stable Diffusion WebUI

* Datasets
  * Quantity and quality
  * Image resolution
* LoRA structure
* Captions
* Starting with a base model
  * `runwayml/stable-diffusion-v1-5` (default)
* Generating captions with Computer Vision models
* Referencing images for styles
* Installing [Dreambooth](https://github.com/d8ahazard/sd_dreambooth_extension) extension
  * Using the [Full SD1.5 model](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors?download=true) as a base
  * [Tutorial](https://github.com/d8ahazard/sd_dreambooth_extension/wiki/ELI5-Training)
* The training job
  * Checkpoints
  * Samples
  * Steps
  * Intervals
  * Batches
  * Learning Rate
  * Image Processing
  * Concepts
  * Filewords
  * Prompts
  * Image Generation
* Fine-tuning the model for a new concept
  * Using a [Google Colab notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb)
    * Make a copy of the notebook and run it in your own environment
    * Use a [Hugging Face Token](https://huggingface.co/settings/tokens) with `write` permissions to save your fine-tuned model and its concepts

## Overview of Computer Vision

* Convolutional Neural Networks (`CNNs`) for image processing
  * CNNs were the first models to achieve state-of-the-art results on computer vision tasks before the rise of transformers-based models
* Vision Transformer (`ViT`)
  * Model that splits images into fixed-size patches and  linearly embed them (flattened and projected into a higher-dimensional space) along with positional encodings to retain information about their original location in the image
    * These embeddings can then be processed by the transformer encoder to perform tasks like the prompts from text generation models or even image generation
* Detecting Transformers (`DETR`)
  * This model uses a Convolutional Neural Network backbone to extract a feature map from the input image, and then this map is then flattened and passed through a series of transformer encoders and decoders to produce the final output
  * The encoder processes the feature map to capture the relationships between different parts of the image, and the decoder takes in a fixed number of learned positional embeddings called "object queries" and decodes them in parallel to predict the classes of the objects and their bounding boxes
* Contrastive Language-Image Pretraining (`CLIP`)
  * When released by OpenAI in 2021, this model greatly improved the state-of-the-art in image classification by combining a vision transformer with a language transformer
  * This model is trained to be multi-modal by using two encoder models that can relate tokens to both images and text
    * This model is trained in a way that it can relate the words to the token representations of images picturing what these words describe
      * For example, the word "dog" would be much closely related to the token representation of an image of a dog than to the token representation of an image of a cat, whereas the word "cat" would be much closely related to the token representation of an image of a cat than to the token representation of an image of a dog
    * This way the model can be used to relate images and texts in both directions

## Computer Vision Models

* Computer Vision (CV)
* Model training
* Inference
* Image Processing tasks (prompts)
* Using Transformers for CV
  * Image classification
    * A process in computer vision where an algorithm is trained to recognize and categorize images into predefined classes or labels
      * For example, classifying an image as a "cat," "dog," or "car."
  * Image segmentation
    * Image segmentation involves dividing an image into multiple segments or regions based on specific criteria, such as objects, boundaries, or pixel similarities
  * Video classification
    * Similar to image classification, video classification involves analyzing video frames to categorize the entire video or its segments into predefined classes
    * Video classification considers temporal information and may involve recognizing actions, events, or behaviors over time
      * For example, classifying a video as "sports," "news," or "entertainment."
  * Object detection
    * Object detection is the task of identifying and localizing specific objects within an image or video frame
    * It involves drawing bounding boxes around the detected objects and assigning them corresponding labels
      * For example: detecting and localizing cars, pedestrians, and traffic signs in an autonomous driving scenario.
  * Zero-shot detection
    * Zero-shot detection refers to the ability of a model to recognize and locate objects it has never seen during training
      * This is achieved by using prior knowledge, like the semantic relationship between objects or attributes, to infer the presence of unseen classes without explicit examples
  * Zero-shot classification
    * Zero-shot classification is similar to zero-shot detection but focuses on assigning labels to images or videos without having seen training examples of those specific classes
    * It relies on utilizing semantic information or descriptions of the unseen classes to make predictions
      * For example, classifying an image as a "giraffe" based on its description, even though the model has never been trained on giraffe images
  * Single shot and Few-shot detections and classifications
    * Single-shot and few-shot detection and classification refer to the ability of a model to detect or classify objects with minimal training examples
    * Single-shot detection and classification aim to perform these tasks with a single training example per class, while few-shot detection and classification use a few examples per class
      * These approaches are useful for scenarios where collecting large amounts of labeled data is challenging or expensive
* Using the [Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2205.06230) (`OWL-ViT`) model with [Hugging Face Transformers](https://huggingface.co/docs/transformers/en/model_doc/owlvit)
* Using the [CLIP](https://www.pinecone.io/learn/series/image-search/clip/) model with [Hugging Face Transformers](https://huggingface.co/docs/transformers/en/model_doc/clip#usage-tips-and-example)
  * Interacting with CLIP in [Google Colab](https://colab.research.google.com/github/mlfoundations/open_clip/blob/master/docs/Interacting_with_open_clip.ipynb)
* Running [Zero-Shot](https://huggingface.co/tasks/zero-shot-classification) tasks for [Image Classification](https://huggingface.co/tasks/zero-shot-image-classification) and [Object Detection](https://huggingface.co/tasks/zero-shot-object-detection) with Hugging Face Transformers

## Running Computer Vision Tasks with Hugging Face Transformers

* Practical exercises
  * Exercise 1: Run a [Zero-shot object detection pipeline](./project/00-Object-Detection.md)
    * Code [ObjectDetection.py](./project/ObjectDetection.py) and run it to test the model with a sample image
  * Exercise 2: Run a [Zero-shot image classification pipeline](./project/01-Image-Classification.md)
    * Code [ImageClassification.py](./project/ImageClassification.py) and run it with a file as an argument to output a description of the image
  * Exercise 3: Run the [CLIP-Explainability](./project/02-CLIP-Explainability.md) Notebook

## Next Steps

* Experimenting with more Computer Vision models
* Using computer vision inside an application
* Wrapping up all of the bootcamp content
