# Lesson 07: Using Text Generation WebUI

TODO

## Pre-requisites

TODO

## Review of Lesson 06

TODO

## Exploring different models

In the last lesson we've seen how to use Text Generation WebUI application to run GPT models in our own devices for processing text generation tasks.

Today we're going to explore more of the many features of this tool and see how we can use it to run different models and tasks.

* Downloading Models using the [Model Hub](https://github.com/oobabooga/text-generation-webui/wiki/04-%E2%80%90-Model-Tab#download-model-or-lora) from Hugging Face
* Model configurations
* Model loaders
* Selecting models
* Finding good instruction-following models
* Running different tasks

## Chatting with a local GPT model

* Practical exercises
  * Exercise 1: [Using Chat Text Generation](./project/00-Chat-Text-Generation.md)
  * Exercise 2: [Using Instruct Text Generation](./project/01-Instruct-Text-Generation.md)
  * Exercise 3: [Using Chat-Instruct Text Generation](./project/02-Chat-Instruct-Text-Generation.md)
  * Exercise 4: [Using the Notebook mode](./project/03-Notebook-Mode.md)

## More features

* Using [Extensions](https://github.com/oobabooga/text-generation-webui/wiki/07-%E2%80%90-Extensions#built-in-extensions)
* Using the [API flag](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API)
* [Fine tuning](https://github.com/oobabooga/text-generation-webui/wiki/05-%E2%80%90-Training-Tab) models

## Replacing the OpenAI APIs

Now that we have a tool to run GPT models in our own devices, we can run the `Text Generation` tasks services and serve these with a local API.

By using the built-in OpenAI API Extension from Text Generation WebUI, we can now replace the OpenAI APIs calls inside our scripts and applications to call this local API.

* Practical exercises
  * Exercise 5: [Using the Text Generation WebUI API](./project/04-Using-API.md) as a replacement for OpenAI APIs in a python script

## Next steps

TODO
