Tutorial link: https://sdk.vercel.ai/docs/guides/providers/openai

1. **Create your project**: This will set up a new project for you using Next.js, a popular framework for building web applications. Open your terminal and type the following command:

    `npx create-next-app my-ai-app`

2. **Choose all default options**: The command will ask you a series of questions. For now, just press the 'Enter' key each time to select the default options

3. **Navigate to the created folder**: The command you ran in step 1 created a new folder called 'my-ai-app'. You need to navigate into this folder using the following command:

    `cd my-ai-app`

4. **Open the project in VSCode**: Visual Studio Code (VSCode) is a code editor where you can write and manage your code. Open your project in VSCode with the following command:

    `code .`

    Alternatively, you can open it manually. Find the 'my-ai-app' folder on your computer, right-click it, and choose 'Open with VSCode'

5. **Install the suggested dependencies**: These are the libraries that your project needs to run. Install them with the following command:

    `npm install ai openai`

6. **Create a `.env` file**: This is a special file where you can store things like API keys. In the root folder of your project, create a new file named `.env`

7. **Paste the API key**: You need an API key to use OpenAI's services. For now, paste `OPENAI_API_KEY=xxx` into the `.env` (to save the file, press 'Ctrl + S')

8. **Get an API Key**: This is the same key you set up in Exercise 2 of Lesson 01. If you've lost it, don't worry. You can get a new one from https://platform.openai.com/api-keys.

9. **Replace the placeholder key**: In the `.env` file, replace `xxx` with the OpenAI API key you got in the previous step and save the file