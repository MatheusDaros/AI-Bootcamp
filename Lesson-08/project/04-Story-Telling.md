# Building a Storytelling Application

1. Start a new project with the NextJS AI SDK

  * Follow the same instructions from exercise 02-Vercel-NextJS-AI-SDK from Lesson 05, but use a different project name in the create command. For example:

    `npx create-next-app story-telling-app`

2. Update the 'page.tsx' file with an explanation about the app

   * Example:

   ````tsx
   export default function Chat() {
       const { messages, isLoading, append } = useChat ();

       ...

       return (
          <div>
          <h1>Storytelling Application</h1>
          <p>
             This application uses AI to generate stories based on user input. Select a genre and tone for the story, and the AI will create a short story for you.
          </p>
          </div>
       );
    }
    ````

3. Include a dropdown of story genres for the user to select

   * For example, fantasy, mystery, romance, and science fiction

   ```tsx
   const [genre, setGenre] = useState("fantasy");

   ...

   <select
     value={genre}
     onChange={(e) => setGenre(e.target.value)}
   >
       <option value="fantasy">Fantasy</option>
       <option value="mystery">Mystery</option>
       <option value="romance">Romance</option>
       <option value="science fiction">Science Fiction</option>
   </select>
   ```

4. Include a radio button for the user to select the tone of the story

   * For example, happy, sad, funny, and scary

   ```tsx
   const [tone, setTone] = useState("happy");

   ...

   <input
     type="radio"
     id="happy"
     name="tone"
     value="happy"
     checked={tone === "happy"}
     onChange={(e) => setTone(e.target.value)}
   />
   <label htmlFor="happy">Happy</label>
   <input
     type="radio"
     id="sad"
     name="tone"
     value="sad"
     checked={tone === "sad"}
     onChange={(e) => setTone(e.target.value)}
   />
   <label htmlFor="sad">Sad</label>
   <input
     type="radio"
     id="funny"
     name="tone"
     value="funny"
     checked={tone === "funny"}
     onChange={(e) => setTone(e.target.value)}
   />
   <label htmlFor="funny">Funny</label>
   <input
     type="radio"
     id="scary"
     name="tone"
     value="scary"
     checked={tone === "scary"}
     onChange={(e) => setTone(e.target.value)}
   />
   <label htmlFor="scary">Scary</label>
   ```

5. Include a button for the user to generate the story

   * Example:

   ```tsx
   <button
     onClick={() => append({
             role: "user",
             content:
               `Create a short ${genre} story with a ${tone} tone.`,
           })}>
     Generate Story
   </button>
   ```

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
           `You are a professional storyteller who has been hired to write a series of short stories for a new anthology. The stories should be captivating, imaginative, and thought-provoking. They should explore a variety of themes and genres, from science fiction and fantasy to mystery and romance. Each story should be unique and memorable, with compelling characters and unexpected plot twists.`,
       },
       ...messages,
     ],
   });
   ```

7. Test the app to evaluate how the AI responds to the user's requests

   * Run the app by executing the following command in the terminal:

   ```bash
   npm run dev
   ```
