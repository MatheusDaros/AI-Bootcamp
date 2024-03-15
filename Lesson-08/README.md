# Lesson 08: Building our first local AI application

In Lesson 08, we'll explore creating our first local AI application. Throughout the lesson, we will understand how to integrate local AI services into our applications, allowing us to perform text generation tasks directly on our own devices.

During the lesson, we will perform practical exercises with a local API in our NextJS application, exploring the text generation capabilities offered by GPT templates. 

We will also analyze the quality and accuracy of text generation, identifying the areas where GPT models are most effective and those where they can be improved. Finally, we will create a storytelling application using NextJS and a local API, consolidating the concepts learned during the lesson and preparing for more advanced projects.

## Pre-requisites

* Learn how to use a shell/terminal/console/bash in your device
  * Get familiar with basic commands like `cd`, `ls` and `mkdir`
  * Learn how to execute packages, scripts and commands in your device
* Install Node.js in your device
  * [Node.js](https://nodejs.org/en/download/)
* Learn how to use `npm` and `npx` commands
  * Docs: [npm](https://docs.npmjs.com/)
  * Docs: [npx](https://www.npmjs.com/package/npx)
* Learn how to use `npm install` and how to deal with `node_modules` folder
  * Docs: [npm install](https://docs.npmjs.com/cli/v10/commands/npm-install)
* Install `git` CLI in your device
  * [Git](https://git-scm.com/downloads)
* Learn how to use `git` commands to clone repositories
  * Docs: [Git](https://git-scm.com/doc)
* Install Next.js in your device
  * [Next.js installation](https://nextjs.org/docs/getting-started/installation)
* Learn about the Next.js
  * Docs: [Next.js](https://nextjs.org/docs)


## Review of Lesson 07

* Executing various GPT models and tasks
* Interacting with a local GPT model
* Using the Text Generation WebUI API as an alternative to OpenAI APIs

## Building applications using local AI services

In the last lesson we've seen how to use Text Generation WebUI application to run GPT models in our own devices for processing text generation tasks.

We even completed an exercise to call the local API from a python script, where we could serve the text generation task from a local service running the Text Generation WebUI application.

Now that we have this capability, we can use it inside applications we're running in our local environment as well.

Later on, when deploying our applications to the cloud, we can use the same technique to serve the text generation tasks from a cloud service, exposing the API server to the internet, authenticating our own users with our own logic, and getting rid of OpenAI's API calls entirely.

## Using a local API Chat Completion tasks

* Practical exercises
  * Exercise 1: [Replacing OpenAI's Chat Completion API with a local API](./project/00-Chat-Completion.md) in our `Chef GPT` NextJS application

## Exploring AI possibilities with local APIs

Now that we've seen how to easily create web application using modern web development frameworks, and now that we have a local API to serve text generation tasks, we can put these concepts together and start creating applications to explore more and more of what AI can do.

Since the number of tokens passed/generated from AI Tasks in OpenAI API calls is directly related to the bills we're charged for using the models, it's normal that we refrain from overdoing our experiments with it.

But now that we have a local environment for running these tasks at marginal costs (like electricity and hardware costs), we can start exploring in depths what we can do with these models.

## Testing prompts

* Practical exercises
  * Exercise 2: [Testing prompts formats and techniques](./project/01-Testing-Prompts.md) for text generation tasks
  * Exercise 3: [Building a prompt to fact-check statements](./project/02-Fact-Checking.md)
  * Exercise 4: [Building a prompt to generate stories](./project/03-Story-Generation.md)

## Text generation quality and precision

* What GPTs are usually good for
* What GPTs are usually not so good for
* Getting the best of LLMs
* Using LLMs for creative writing

## Creating an application for telling stories

* Practical exercises
  * Exercise 5: [Building a story telling application](./project/04-Story-Telling.md) using NextJS and a local API for text generation tasks

## Weekend project

For consolidating the knowledge acquired in this week, the students should complete the following project:

1. Create a github repository for your project
2. Add all members of your group
3. Create a README.md file with the description of your project
4. Create a new application from scratch using NextJS
5. Create a page for generating jokes using AI
6. Add a feature for users to customize the Joke Parameters

   * You can pick what kind of parameters you would like to offer for your users
   * For example, you could allow users to pick a topic from a list of options (work, people, animals, food, television, etc), a tone for the joke (witty, sarcastic, silly, dark, goofy, etc), the kind of joke (pun, knock-knock, story, etc), and the "temperature" of it (how much randomness/fun you want to add to the joke)
   * Consider how you're going to assemble the prompt for the AI model to abide to these parameters

7. After configuring the parameters, users should click a button to generate the joke, and the generated response must be returned to the user's screen inside the same page
8. Add a feature for the AI to evaluate if the generated jokes are funny or not, appropriated or not, offensive or not, and other criteria you might judge important
9. Run the Text Generation WebUI application in your local environment and use it to serve the text generation tasks for your application
10. Submit your project in the submission form

>You should find your group in the [Discord](https://discord.gg/encodeclub) AI Bootcamp Channel
>>If you can't find your group, please contact the program manager through Discord or email

## Next steps

* Implementing GPT models;
* Training with GPT;
* Experimenting with GPT-2 and Fine-tuning GPT-2;
* Practical exercises;
