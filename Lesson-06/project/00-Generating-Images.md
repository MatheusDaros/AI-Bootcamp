# Extending the Chef GPT App with Image Generation

1. Open the Chef GPT page we created in the last lesson on your IDE

2. Remove the text input to enter messages

   * Remove this part of the code:

     ```html
     <form onSubmit={handleSubmit} className="flex justify-center">
          <input
            className="w-[95%] p-2 mb-8 border border-gray-300 rounded shadow-xl text-black"
            disabled={isLoading}
            value={input}
            placeholder="Say something..."
            onChange={handleInputChange}
          />
     </form>
     ```

3. After the user clicks on "Random Recipe", change the button text to "Generate Image"

   * Change the `Random Recipe` code to:

     ```tsx
     <div className="flex flex-col justify-center mb-2 items-center">
       {messages.length == 0 && (
         <button
           className="bg-blue-500 p-2 text-white rounded shadow-xl"
           disabled={isLoading}
           onClick={() =>
             append({ role: "user", content: "Give me a random recipe" })
           }
         >
           Random Recipe
         </button>
       )}
       {messages.length == 2 && !isLoading && (
         <button
           className="bg-blue-500 p-2 text-white rounded shadow-xl"
           disabled={isLoading}
           onClick={() => {}}
         >
           Generate image
         </button>
       )}
     </div>
     ```

4. When the user clicks the button, the app should call the OpenAI API to generate an image for the dish

   * Create a new folder called `images` under the `api` folder

   * Add a file named `route.ts` inside the `images` folder

   * Add this code to the `route.ts` file:

     ```ts
     import OpenAI from "openai";
     
     const openai = new OpenAI({
       apiKey: process.env.OPENAI_API_KEY,
     });
     
     export const runtime = "edge";
     
     export async function POST(req: Request) {
       const { message } = await req.json();
       const prompt = `Generate an image that describes the following recipe: ${message}`;
       const response = await openai.images.generate({
         model: "dall-e-2",
         prompt: prompt.substring(0, Math.min(prompt.length, 1000)),
         size: "1024x1024",
         quality: "standard",
         response_format: "b64_json",
         n: 1,
       });
       return new Response(JSON.stringify(response.data[0].b64_json))
     }
     
     ```

   * Fill the function in the `onClick` event of the button to call the `images` API we have just created by passing the last message in the body

     ```tsx
     async () => {
       const response = await fetch("api/images", {
         method: "POST",
         headers: {
           "Content-Type": "application/json",
         },
         body: JSON.stringify({
           message: messages[messages.length - 1].content,
         }),
       });
       const data = await response.json();
       console.log(data);
     };
     ```

5. Display a loading spinner while the image is being generated

   * Add the `useState` import from `react`

   * Add a new state to keep track of the image loading state after the `useChat` hook

     ```tsx
     const [imageIsLoading, setImageIsLoading] = useState(false);
     ```

   * Add `setImageIsLoading(true);` before the fetch call in the `onClick` event of the `Generate image` button

   * Add `setImageIsLoading(false);` after the `console.log(data);` line

   * Add a conditional statement before the `return` statement in the `Chat` component to display the loading animation instead of the chat interface while the image is being generated

     ```tsx
     if (imageIsLoading) {
       return (
         <div className="flex justify-center items-center h-screen">
           <div className="loader">
             <div className="animate-pulse flex space-x-4">
               <div className="rounded-full bg-slate-700 h-10 w-10"></div>
             </div>
           </div>
         </div>
       );
     }
     ```

6. Display the generated image in the page when it's ready

   * Add a new state to keep track of the image URL after the `imageIsLoading` state

     ```tsx
     const [image, setImage] = useState<string | null>(null);
     ```

   * Replace the `console.log(data);` line with `setImage(data);`

   * Add a conditional statement before the `return` statement in the `Chat` component to display the image instead of the chat interface when the image is ready

     ```tsx
     if (image) {
       return (
         <div className="flex justify-center items-center h-screen">
           <img src={`data:image/jpeg;base64,${image}`} />
         </div>
       );
     }
     ```

7. Display the recipe for that dish below the image in a text area

   * Add a text box below the image in the conditional statement

     ```tsx
     <div className="flex justify-center items-center h-screen">
       <img src={`data:image/jpeg;base64,${image}`} />
       <textarea
          className="w-full text-white bg-black"
          value={messages[messages.length - 1].content}
          readOnly
       />
     </div>
     ```

   * Modify the `div` above with the `card` class to display the image and the recipe one below the other

     ```tsx
     <div className="card w-full h-screen max-w-md py-24 mx-auto stretch">
       <img src={`data:image/jpeg;base64,${image}`} />
       <textarea
         className="mt-4 w-full text-white bg-black"
         value={messages[messages.length - 1].content}
         readOnly
       />
     </div>
     ```

8. Check if your `page.tsx` code is complete

   * The `page.tsx` file should look like this:

     ```tsx
     "use client";

     import { useChat } from "ai/react";
     import { useEffect, useRef, useState } from "react";
     
     export default function Chat() {
       const {
         messages,
         isLoading,
         append,
       } = useChat();
     
       const [imageIsLoading, setImageIsLoading] = useState(false);
       const [image, setImage] = useState<string | null>(null);
     
       const messagesContainerRef = useRef<HTMLDivElement>(null);
     
       useEffect(() => {
         if (messagesContainerRef.current) {
           messagesContainerRef.current.scrollTop =
             messagesContainerRef.current.scrollHeight;
         }
       }, [messages]);
     
       if (imageIsLoading) {
         return (
           <div className="flex justify-center items-center h-screen">
             <div className="loader">
               <div className="animate-pulse flex space-x-4">
                 <div className="rounded-full bg-slate-700 h-10 w-10"></div>
               </div>
             </div>
           </div>
         );
       }
     
       if (image) {
         return (
           <div className="card w-full h-screen max-w-md py-24 mx-auto stretch">
             <img src={`data:image/jpeg;base64,${image}`} />
             <textarea
               className="mt-4 w-full text-white bg-black h-64"
               value={messages[messages.length - 1].content}
               readOnly
             />
           </div>
         );
       }
     
       return (
         <div className="flex flex-col w-full h-screen max-w-md py-24 mx-auto stretch">
           <div className="overflow-auto mb-8 w-full" ref={messagesContainerRef}>
             {messages.map((m) => (
               <div
                 key={m.id}
                 className={`whitespace-pre-wrap ${
                   m.role === "user"
                     ? "bg-green-700 p-3 m-2 rounded-lg"
                     : "bg-slate-700 p-3 m-2 rounded-lg"
                 }`}
               >
                 {m.role === "user" ? "User: " : "AI: "}
                 {m.content}
               </div>
             ))}
     
             {isLoading && (
               <div className="flex justify-end pr-4">
                 <span className="animate-bounce">...</span>
               </div>
             )}
           </div>
           <div className="fixed bottom-0 w-full max-w-md">
             <div className="flex flex-col justify-center mb-2 items-center">
               {messages.length == 0 && (
                 <button
                   className="bg-blue-500 p-2 text-white rounded shadow-xl"
                   disabled={isLoading}
                   onClick={() =>
                     append({ role: "user", content: "Give me a random recipe" })
                   }
                 >
                   Random Recipe
                 </button>
               )}
               {messages.length == 2 && !isLoading && (
                 <button
                   className="bg-blue-500 p-2 text-white rounded shadow-xl"
                   disabled={isLoading}
                   onClick={async () => {
                     setImageIsLoading(true);
                     const response = await fetch("api/images", {
                       method: "POST",
                       headers: {
                         "Content-Type": "application/json",
                       },
                       body: JSON.stringify({
                         message: messages[messages.length - 1].content,
                       }),
                     });
                     const data = await response.json();
                     setImage(data);
                     setImageIsLoading(false);
                   }}
                 >
                   Generate image
                 </button>
               )}
             </div>
           </div>
         </div>
       );
     }

     ```

9. Test the app by running `npm run dev` in your terminal and navigating to <http://localhost:3000`> in a browser

10. Always remember to check the AI generated instructions, as they may contain errors, misleading information, or even inappropriate/harmful content

    * If you test the recipes generated and they turn out to be good ones, make sure to invite me to dinner! 🍽️
