# Building a Storytelling Application

1. Start a new project with the NextJS AI SDK template

2. Update the 'page.tsx' file with an explanation about the app

3. Include a dropdown of story genres for the user to select

   * For example, fantasy, mystery, romance, and science fiction

4. Include a radio button for the user to select the tone of the story

   * For example, happy, sad, funny, and scary

5. Include a button for the user to generate the story

6. Set up the AI to act as a storyteller

   * Edit the code that creates chat completions in the 'route.tsx' file inside the 'src/app/api/chat' folder

   ```typescript
   const response = await openai.chat.completions.create({
     model: "gpt-3.5-turbo",
     stream: true,
     messages: [
       {
         role: "system",
         content:
           `You are a professional storyteller who has been hired to write a series of short stories for a new anthology. The stories should be captivating, imaginative, and thought-provoking. They should explore a variety of themes and genres, from science fiction and fantasy to mystery and romance. Each story should be unique and memorable, with compelling characters and unexpected plot twists. Create a short ${genre} story with a ${tone} tone.`,
       },
       ...messages,
     ],
   });
   ```

7. Test the app to evaluate how the AI responds to the user's requests

   * Run the app by executing the following command in the terminal:

   ```bash
   npm start
   ```
