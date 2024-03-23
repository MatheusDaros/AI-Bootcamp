# Creating an Application with Vercel AI SDK

1. Create your project

   * This will set up a new project for you using Next.js templates

   * Open your terminal and type the following command:

    `npx create-next-app my-ai-app`

2. Choose all default options

   * When asked `Ok to proceed? (y)` press 'Enter' to confirm

   * When asked `Would you like to use TypeScript? › No / Yes` pick default option `Yes`

   * When asked `Would you like to use ESLint? › No / Yes` pick default option `Yes`

   * When asked `Would you like to use Tailwind CSS? › No / Yes` pick default option `Yes`

   * When asked `Would you like to use src/ directory? › No / Yes` pick default option `No`

   * When asked `Would you like to use App Router? (recommended) › No / Yes` pick default option `Yes`

   * When asked `Would you like to customize the default import alias (@/*)?` pick default option `No`

   * Wait for the installation to finish

3. Navigate to the created folder

   * The command you ran in step 1 created a new folder called 'my-ai-app'

   * You need to navigate into this folder using the following command:

    `cd my-ai-app`

4. Install the suggested dependencies

   * These are the libraries that your project needs to run

   * Install them with the following command:

    `npm install ai openai`

   * Wait for the installation to finish

5. Open the project in VSCode

   * Visual Studio Code (VSCode) is a code editor where you can write and manage your code

   * Open your project in VSCode with the following command:

    `code .`

    * Alternatively, you can open it manually by finding the 'my-ai-app' folder on your computer, right-clicking it, and choosing 'Open with VSCode'

    * If you don't have the 'Open with VSCode' option, you can open VSCode and use the 'File' > 'Open Folder' option to navigate to the 'my-ai-app' folder

6. Create a `.env` file

   * This is a special file where you can store things like API keys

   * In the root folder of your project, create a new file named `.env`

7. Paste the API key: You need an API key to use OpenAI's services

   * Paste `OPENAI_API_KEY=xxxxx` into the `.env` and save the file

8. Get an API Key: This is the same key you set up in Exercise 2 of Lesson 01

   * If you have the key set up in your OS environment variables, you can get it by running `echo $OPENAI_API_KEY` in your terminal

     * Even if you have it set up in your environment variables in your development machine, it's a good idea to store it in the `.env` file for this project, since later on you might need to handle different environments (like development, testing, and production) for the same project with NextJS using different `.env` files for each

   * If you've lost you API Key, don't worry, you can get a new one from your [API Keys](https://platform.openai.com/api-keys) configuration page

9. Replace the placeholder key: In the `.env` file, replace `xxxxx` with the OpenAI API key you got in the previous step and save the file

   * Your `.env` file should look something like this: `OPENAI_API_KEY=sk-xxxxxx`

10. Create a new file for instructing NextJS how to handle the API calls to OpenAI:

    * In the root of your project, find the `app` folder and create a new folder inside it named `api`

    * Inside the `api` folder, create another new folder named `chat`

    * Inside the `chat` folder, create a new file named `route.ts`

    * Open the `route.ts` file and paste the code:

    ```typescript
    import OpenAI from 'openai';
    import { OpenAIStream, StreamingTextResponse } from 'ai';
     
    // Create an OpenAI API client (that's edge friendly!)
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });
     
    // IMPORTANT! Set the runtime to edge
    export const runtime = 'edge';
     
    export async function POST(req: Request) {
      const { messages } = await req.json();
     
      // Ask OpenAI for a streaming chat completion given the prompt
      const response = await openai.chat.completions.create({
        model: 'gpt-3.5-turbo',
        stream: true,
        messages,
      });
     
      // Convert the response into a friendly text-stream
      const stream = OpenAIStream(response);
      // Respond with the stream
      return new StreamingTextResponse(stream);
    }
    ```

11. Modify the UI with the chat components:

    * In VSCode, open the file 'page.tsx' inside the folder 'app'

    * Replace the existing code with the following:

    ```typescript
    'use client';
     
    import { useChat } from 'ai/react';
     
    export default function Chat() {
      const { messages, input, handleInputChange, handleSubmit } = useChat();
      return (
        <div className="flex flex-col w-full max-w-md py-24 mx-auto stretch">
          {messages.map(m => (
            <div key={m.id} className="whitespace-pre-wrap">
              {m.role === 'user' ? 'User: ' : 'AI: '}
              {m.content}
            </div>
          ))}
     
          <form onSubmit={handleSubmit}>
            <input
              className="fixed bottom-0 w-full max-w-md p-2 mb-8 border border-gray-300 rounded shadow-xl text-black"
              value={input}
              placeholder="Say something..."
              onChange={handleInputChange}
            />
          </form>
        </div>
      );
    }
    ```

12. Run the application: Now that everything is set up, you can start your application

    * On your terminal, run the following command:

    `npm run dev`

    * If everything is okay, you can now access the application at <http://localhost:3000/>

>You can check the official tutorial from Vercel at <https://sdk.vercel.ai/docs/guides/providers/openai>
