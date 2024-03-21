# Lesson 15: AI Image Processing

In this lesson we'll learn about more extensions to image generation models, like generating videos frame-by-frame with the help of ControlNets, and how to fine-tune models to generate images with more precision using curated datasets.

We're going to explore how models can be fine-tuned and enhanced using LoRAs and VAEs to greatly extend their image generation capabilities. We'll experiment with image datasets and techniques to properly correlate elements in an image to approximated text descriptions.

By the second half of this lesson we're going to explore more on the idea of extracting information from images, and we're going to learn about a technique called "Computer Vision" and how it can be used to process text from images.

We're going to see an overview on how the same versatile Transformers architecture we've been seeing before for text and image generation can be used again for image processing tasks. We're going to experiment using transformers to run Zero-shot detection and classification tasks to better understand what computer vision can do.

Finally, we're going to learn how to install and use the Vision Process WebUI to run computer vision tasks on our own devices.

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
* Install [EbSynth](https://github.com/s9roll7/ebsynth_utility) extension in Stable Diffusion WebUI and all the correct dependencies
* Install [Dreambooth](https://github.com/d8ahazard/sd_dreambooth_extension) extension in Stable Diffusion WebUI and all the correct dependencies
* Install the [Transformers](https://huggingface.co/docs/transformers/main/en/installation) library on your environment
* Install [Vision Process WebUI](https://github.com/isLinXu/vision-process-webui) on your device and all the correct dependencies for your hardware

## Review of Lesson 14

* Prompt engineering for image generation
* Configuring Stable Diffusion WebUI
* Capabilities and limitations of stable diffusion models
* Using ControlNet to guide the diffusion process
* ControlNet extension for Stable Diffusion WebUI

## Using ControlNet to Generate Videos

* Stable Video Diffusion
* Generating videos frame by frame
* [EbSynth](https://github.com/s9roll7/ebsynth_utility) extension
* Using `canny` and `maps` for edge and depth detection

## Fine-Tuning Models with Stable Diffusion WebUI

* Datasets
  * Quantity and quality
  * Image resolution
* LoRA structure
* Captions
* Starting with a base model
  * `runwayml/stable-diffusion-v1-5` (default)
  * `SG161222/Realistic_Vision_V2.0` for photorealistic images
  * `Linaqruf/anything-v3.0` for art, anime and cartoons
* Generating captions with Computer Vision models
* Referencing images for styles
* [Dreambooth](https://github.com/d8ahazard/sd_dreambooth_extension) extension
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

## Overview of Computer Vision

* Convolutional Neural Networks (`CNNs`) for image processing
  * CNNs were the first models to achieve state-of-the-art results on computer vision tasks before the rise of transformers-based models
* Vision Transformer (`ViT`)
  * Model that split images into fixed-size patches and  linearly embed them (flattened and projected into a higher-dimensional space) along with positional encodings to retain information about their original location in the image
    * These embeddings can then processed by the transformer encoder to perform tasks like the prompts from text generation models or even image generation
* Detecting Transformers (`DETR`)
  * This model uses a convolutional neural network (CNN) backbone to extract a feature map from the input image, and then this map is then flattened and passed through a series of transformer encoders and decoders to produce the final output
  * The encoder processes the feature map to capture the relationships between different parts of the image, and the decoder takes in a fixed number of learned positional embeddings called "object queries" and decodes them in parallel to predict both the classes and bounding boxes of the objects

## Computer Vision Models

* Computer Vision (CV)
* Model training
* Inference
* Image Processing tasks (prompts)
* Using Transformers for CV
  * Image classification
  * Image segmentation
  * Video classification
  * Object detection
  * Zero-shot detection
  * Zero-shot classification
  * Image processing
* Using the [Simple Open-Vocabulary Object Detection with Vision Transformers](https://arxiv.org/abs/2205.06230) model

## Running CV Tasks with Hugging Face Transformers

* Practical exercises
  * Exercise 1: Run a [Zero-shot object detection pipeline](./project/00-Object-Detection.md)
    * Code [ObjectDetection.py](./project/ObjectDetection.py) and run it one object name and a file as argument to output an image with the object detected inside a box
  * Exercise 2: Run a [Zero-shot image classification pipeline](./project/01-Image-Classification.md)
    * Code [ImageClassification.py](./project/ImageClassification.py) and run it with a file as argument to output a description of the image

## Identifying Images with the Vision Process WebUI

* The [Vision Process WebUI](https://github.com/isLinXu/vision-process-webui)
* Dependencies
* Installation
* Features
  * Object detection
  * Image classification
  * Image segmentation
  * OCR
* Models

## Running CV Tasks with Vision Process WebUI

* Practical exercises
  * Exercise 3: Run the [Classification](./project/02-Image-Classification-WebUI.md) task in an image
  * Exercise 4: Run the [Object Detection](./project/03-Object-Detection-WebUI.md) task in an image

## Next Steps

* Experimenting with more Computer Vision models
* Using the Vision Process WebUI for more computer vision tasks
* Using computer vision inside an application
* Wrapping up all of the bootcamp content
