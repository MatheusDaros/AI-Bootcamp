# Lesson 13: Running Stable Diffusion Model Locally

In this lesson, we will explore more about AI Image Generation with Stable Diffusion models by running these models locally on our own devices.

We're going to use different models and techniques for text-to-image generation tasks. We'll use the Stable Diffusion WebUI tool, which can handle many complex tasks needed to run these models and provides a simple, intuitive interface for interaction.

While we use the Stable Diffusion WebUI, we'll learn about some technical details of how stable diffusion models workand the possible configurations and parameters to optimize these models for our hardware. We'll also learn about the various sampling and denoising algorithms that can be used to generate images, and how to use the API for a more programmatic approach.

By the end of this lesson, we'll explore various types of models and checkpoints publicly available to download from public hubs. We'll also test the limitations and capabilities of some of these models.

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
    * Make sure you have a GPU with at least 4GB of Dedicated GPU virtual memory, since this is  pre-requisite to run most models locally

## Review of Lesson 12

* Weekend project review
* AI Image Generation
* Stable Diffusion overview
* Using DALI·E model from OpenAI

## Setting Up Stable Diffusion WebUI

* The [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) tool
  * Inspired the `Text Generation WebUI` we used before
  * Built on [Gradio](https://www.gradio.app/) as well
  * Similar interface
  * Similar usage
* Dealing with the [Dependencies](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Dependencies)
  * Instructions for [NVidia](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-NVidia-GPUs)
  * Instructions for [AMD](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs)
  * Instructions for [Intel](https://github.com/openvinotoolkit/stable-diffusion-webui/wiki/Installation-on-Intel-Silicon)
  * Instructions for [Apple](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-on-Apple-Silicon)
  * Options for running in [Docker Containers](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Containers)
  * Options for running in [Online Services](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Online-Services)
* Instructions for [Installing and Running](https://github.com/AUTOMATIC1111/stable-diffusion-webui?tab=readme-ov-file#installation-and-running)
* Usage
  * Access the WebUI at <http://127.0.0.1:7860/> (default location)
  * Run with the `--api` flag to access the API at <http://127.0.0.1:7860/docs>
* Main [Features](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features)
* Using Models and Checkpoints

## Generating Images with Stable Diffusion WebUI

* Selecting a Model (checkpoint)
  * The starting model is the "classic" `runwayml/stable-diffusion-v1-5` [Model](https://huggingface.co/runwayml/stable-diffusion-v1-5) that we used in previous examples
  * Specifically, the version used is `v1-5-pruned-emaonly`, that is not suitable for fine-tuning, but it's ideal for inference (generating images), since it uses less VRAM
    * The "full" `v1-5-pruned` version is suitable for fine-tuning, but it uses more VRAM
      * The term "ema-only" refers to the fact that the model uses only the Exponential Moving Average (EMA) of the weights, which is a technique used to stabilize the training of the model
      * The "full" version has all the weights, including the EMA and the non-EMA, and thus uses more VRAM to be processed, but also provides more flexibility for fine-tuning
    * Pruned means that the model has been pruned to remove unnecessary/irrelevant weights, which makes it smaller and faster to process with almost negligible losses of performance/precision
  * To summarize, you can use the starting model to generate images, but consider changing it before attempting to fine-tune anything
* Passing a prompt
  * Similar to the `Text Generation WebUI`, you can pass a prompt to the model to generate an image
  * We're going to see more about this in practice later on
* Configuring the image generation options
  * Width and height: The size of the output image
    * For example, you can set the width to 512 and the height to 384 to generate a 4:3 aspect ratio image, or for portrait images, you can set the width to 512 and the height to 768 for a 2:3 aspect ratio
  * Batch size: Number of images to be generated each time
    * This consumes more VRAM, but it's often much more practical to generate multiple images at once and discard unsatisfactory ones, rather than generating them one by one repeatedly until you achieve a good result
* Configuring the sampling options
  * Sampling steps: The fixed number of steps to sample the image
    * Generally, the more steps, the more detailed the image will be, but also the longer it will take to generate
    * At some point, adding more steps will not make a noticeable difference in the image quality, and could even start to degrade it in some algorithms
  * Sampling method: What algorithm to use to sample the image on each step
    * Old-School ODE solvers: ODEs (Ordinary Differential Equation) solvers are numerical methods used to solve differential equations, which are mathematical equations that relate some function with its derivatives
      * `Euler`: The simplest possible solver, which approximates the solution of an ODE by using finite differences to approximate the derivative
      * `Heun`: A more accurate but slower version of Euler that uses a second-order Runge-Kutta method used for the numerical solution of initial value problems
      * `LMS` (Linear multi-step method): A class of numerical techniques used to solve Ordinary Differential Equations that use multiple previous points to calculate the next point in the solution, hence the name "multi-step"
    * Ancestral samplers: A group of stochastic samplers that adds noise to the image at each sampling step, adding some randomness to the final image
      * Methods with the notation `a` (ancestral) in the name like `Euler a`, `DPM2 a`, `DPM++ 2S a` and `DPM++ 2S a Karras` all fall in this category
      * These models are generally faster to process, but they can produce more noisy results, and the outputs may vary a lot from one run to another
    * `Karras` noise schedule: A method developed by Tero Karras, the creator of the StyleGAN model, to add noise to the image at each sampling step
      * The key insight from Karras et al. was that carefully controlling this noise input could significantly improve the variety and realism of the generated images without compromising overall image quality
      * To implement the Karras noise schedule in practice, one typically initializes the noise scaling factors (also called noise strengths) and learns them during the training process
        * The network then adjusts these factors dynamically, determining the right amount of noise to add at each level of detail in the generated images
      * This method is generally slower to process, but it produces more consistent and less noisy results, and the outputs are more predictable from one run to another
    * `DDIM` (Denoising Diffusion Implicit Models) are a variant of denoising diffusion probabilistic models that use a non-Markovian variant of the reverse process in diffusion models that can generate samples significantly faster than the original approach
      * DDIMs use a deterministic sampling process, which allows for the generation of high-quality samples in fewer steps
        * The "implicit" part of the name comes from the fact that the model does not explicitly learn the density function of the data, but rather learns to generate samples from it
        * This method has been shown to generate high-quality images and has the advantage of being relatively simple and easy to train
    * `PLMS` (Pseudo Linear Multi-Step): A variant of the linear multi-step method that uses a pseudo-linear approach to sample the image at each step
      * This method is similar to the linear multi-step method, but it uses a probabilistic approach to sample the image, which sometimes makes it faster to process than the original LMS method
    * Diffusion Probabilistic Models: a class of generative models that use a diffusion process to generate new data samples, starting from random noise and gradually refining it into a coherent image by iteratively applying a denoising process
      * `DPM` (Diffusion Probabilistic Model): This is the basic version of the diffusion model, that uses a Markov chain to model the diffusion process, where each step of the chain adds a small amount of noise to the image
        * The model is trained to reverse this process, starting from a noisy image and gradually denoising it to produce a clear image
      * `DPM-2` (Diffusion Probabilistic Model 2): This is an improvement over the basic DPM that uses a non-Markovian process, which means that each step of the diffusion process depends not only on the current state but also on the previous states
        * This allows the model to capture more complex dependencies in the data and generate more realistic images
      * `DPM++` (Diffusion Probabilistic Model Plus): This is a further improvement over DPM-2 that introduces a new parameterization of the diffusion process that makes the model easier to train and more flexible
        * This allows it to generate even more realistic images and handle a wider range of data distributions
    * `UniPC` (Unified Predictor-Corrector Framework): a training-free framework designed for the fast sampling of diffusion models, which consists of a corrector (UniC) and a predictor (UniP) that share a unified analytical form and support arbitrary orders
      * UniPC is by design model-agnostic, supporting pixel-space/latent-space DPMs on unconditional/conditional sampling
        * It can also be applied to both noise prediction model and data prediction model
      * Compared with previous methods, UniPC converges faster thanks to the increased order of accuracy
  * Comparing sampling methods
    * Comparing [Performance](https://stable-diffusion-art.com/samplers/) and [Quality](https://learn.rundiffusion.com/sampling-methods/)
* Classifier Free Guidance (`CFG`) scale
  * This option can control how closely the model should follow your text prompt during the sampling steps
  * Lower values (close to 1) allows for more freedom, while higher values (above 10) are more restrictive and can interfere with the quality
  * Stable Diffusion may completely ignore your prompt if the CFG value is too low, or the color of the images may become overly saturated when this parameter is too high
    * [Comparison Article](https://www.artstation.com/blogs/kaddoura/pBPo/stable-diffusion-samplers)
* Seed
  * The seed value used to generate the initial random tensor in the latent space
  * This value can be used to reproduce the same or very similar images from the same prompt and settings
  * Using variational seeds can produce interesting results, as if you were exploring a subset of the latent space between two defined seeds
    * This can produce a sort of "blending" effect between two images, and the sequential generations in the middle can appear as a "gradual transformation" from one image to the other
* Built-in extensions
  * Restore faces: a set of scripts and tools that can replace distorted faces in images with more realistic ones
  * Tiling: a technique to change the borders of the image being generated so that it can be repeated seamlessly in a grid
  * High resolution fix: a set of methods and tools to upscale images
    * Generating images in higher resolutions can be quite challenging for the majority of models, and the results are often not as good as the ones in lower resolutions
    * Because of that, you can keep the image generation process with a native resolution of 512 pixels, and then the high resolution fix can be used to improve the quality of the images generated in higher resolutions
* Other tabs
  * Not only can the Stable Diffusion WebUI generate images from texts, but it can also perform many other image generation tasks
  * Image to Image: Generate images from other images
  * Sketch: Generate images from crude drawings or from edited/annotated images
  * Inpainting: Generate images to replace areas of other bigger images
* CLIP (Contrastive Language-Image Pretraining): a tool for extracting a potential prompt that describes an image

## Using Stable Diffusion WebUI API

* Practical exercises
  * Exercise 1: [Generate a simple image](./project/00-Generate-Image.md) from a text input with default settings
  * Exercise 2: [Generate a landscape picture](./project/01-Generate-Landscape.md) with a specific prompt and settings
  * Exercise 3: [Generate a portrait picture](./project/02-Generate-Portrait.md) and inpaint the generated face
  * Exercise 4: [Generate a picture from a sketch](./project/03-Generate-Sketch.md)

## Using Model Checkpoints

* Downloading models
  * From [Hugging Face](https://huggingface.co/models?pipeline_tag=text-to-image&library=diffusers&sort=downloads) (filter for "Diffusers" under "Library")
  * From [CivitAI](https://civitai.com/models?tag=base+model) (filter for "Checkpoints" under "Model Types")
  * Using an [Extension](https://github.com/Iyashinouta/sd-model-downloader)
* Recommendations
  * High resolution model [SDXL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
    * Not good for readable text, faces or object compositionality
  * Standard resolution photorealistic model [Photon](https://civitai.com/models/84728/photon)
    * Has some problems with rendering hands and fingers
  * Versatile model for digital art, drawings, anime and painting [GhostMix](https://civitai.com/models/36520?modelVersionId=76907)
    * Requires the use of LoRAs for perfect results
    * Not very good for photorealistic images, or even to generate images of "common" persons or scenes
  * Versatile high resolution model [JuggernautXL](https://civitai.com/models/133005/juggernaut-xl)
    * Good generalist model that makes good use of light/shadow effects
* Choosing models
  * Model file extensions
    * `ckpt` files are models where python can load serialized data, but they are dangerous since they can execute arbitrary code
    * `safetensors` files are not affected by the vulnerability of `ckpt` files, and are preferred whenever available
  * LoRAs (Low-Rank Adaptation)
    * LoRAs are a set of techniques used to adapt a model to a specific characteristic or dataset
    * Some models include this inside the checkpoint, increasing the quality of the generated images but also decreasing the compatibility with other LoRAs that could be used in conjunction with the model
  * VAEs (Variational autoencoders)
    * Some models require a VAE to be used in conjunction with them to properly generate images
      * The VAE encodes images into a latent space that the model uses during training
      * At generation time, the model decodes points from the latent space back into images
      * Without the matching VAE, the model can’t properly reconstruct the images
    * If a checkpoint says it requires a certain VAE, you need to use that VAE to get proper image generations, otherwise the results will be very poor
  * Model categories
    * `Base` models are the most common and versatile models, and they are the best choice for using as base for fine-tuning
    * `XL` models are high-resolution models that can generate images with more details, but they are also slower to process and require more VRAM
    * `Anime` models are specialized in generating anime-style images
    * `Cartoon` models are specialized in generating cartoon-style images
    * `Art` models are specialized in generating digital art, drawings, paintings, and other artistic styles
    * `Photorealistic` models are specialized in generating images that look like real photographs
    * `Portrait` models are specialized in generating images of people
    * `Hybrid` models are a mix of two or more of the previous categories, and they are the best choice for tasks that require a mix of styles or variety in the generated images
    * [Model Classification](https://civitai.com/articles/1939/an-attempt-at-classification-of-models-sd-v15) article
    * [Model Comparison](https://civitai.com/articles/2044/standardized-prompts-for-efficient-model-testing-a-possible-civitai-test) article

## Next Steps

* Testing different models and checkpoints
* Exploring more about the Stable Diffusion WebUI
* Tweaking configurations and parameters for running models on your device
* Prompting techniques for image generation
* Using Extensions in Stable Diffusion WebUI
* Using a ControlNet to guide the diffusion process
