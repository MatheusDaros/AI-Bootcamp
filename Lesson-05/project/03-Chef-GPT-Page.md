# Building the Chef GPT App

In this exercise, we will enhance our chat application to function as a virtual chef. Here's a step-by-step guide:

1. Update the 'page.tsx' file: Locate the 'page.tsx' file in the 'src/app' folder from the previous exercise. Replace its content with the following code:

   ```typescript
   "use client";
   
   import { useChat } from "ai/react";
   import { useEffect, useRef } from "react";
   
   export default function Chat() {
     const {
       messages,
       input,
       handleInputChange,
       handleSubmit,
       isLoading,
       append,
     } = useChat();
   
    const messagesContainerRef =  useRef<HTMLDivElement>(null);
   
     useEffect(() => {
       if (messagesContainerRef.current) {
         messagesContainerRef.current.scrollTop =
           messagesContainerRef.current.scrollHeight;
       }
     }, [messages]);
   
     return (
      <div className="flex flex-col w-full h-screen  max-w-md py-24 mx-auto stretch">
        <div className="overflow-auto h-[88%]  w-full" ref={messagesContainerRef}>
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
              < className="animate-bounce">...</ span>
             </div>
           )}
         </div>
        <div className="fixed bottom-0 w-full  max-w-md">
          <div className="flex flex-col  justify-center items-center">
             <button
              className="bg-blue-500 p-2 text-white  rounded shadow-xl"
               disabled={isLoading}
               onClick={() =>
                append({ role: "user", content:  "Give me a random recipe" })
               }
             >
               Random Recipe
             </button>
             <p className="p-4">OR</p>
           </div>
          <form onSubmit={handleSubmit}  className="flex justify-center">
             <input
              className="w-[95%] p-2 mb-8 border border-gray-300 rounded shadow-xl  text-black"
               disabled={isLoading}
               value={input}
               placeholder="Say something..."
               onChange={handleInputChange}
             />
           </form>
         </div>
       </div>
     );
   }
   ```

   > This code sets up a chat interface. It includes a text input for user messages and a button to request a random recipe.

2. Understand the changes: We've made a few key additions:

    * Chat bubble styles: We've added styles to make the messages look like chat bubbles

    ```typescript
    className={`whitespace-pre-wrap ${
        m.role === "user"
            ? "bg-green-700 p-3 m-2 rounded-lg"
            : "bg-slate-700 p-3 m-2 rounded-lg"
    }`}
    ```

    * Loading indicator: We've added a loading element to show when the AI is generating a response

    ```typescript
    {isLoading && (
        <div className="flex justify-end pr-4">
            <span className="animate-bounce">...</span>
        </div>
    )}
    ```

    * Random Recipe button: We've added a button that, when clicked, uses the `append` function from our [`useChat`]('https://sdk.vercel.ai/docs/api-reference/use-chat') hook to add a new message to the chat. This message asks the AI for a random recipe

    ```typescript
    <button
      className="bg-blue-500 p-2 text-white rounded shadow-xl"
      disabled={isLoading}
      onClick={() => append({ role: "user", content: "Give me a random recipe" })}
    >
      Random Recipe
    </button>
    ```

3. Set up the AI to act as a chef

   * Now, let's make the AI act like a chef

   * Replace the code that creates chat completions in the 'route.tsx' file inside the 'src/app/api/chat' folder

   ```typescript
   const response = await openai.chat.completions.create({
     model: "gpt-3.5-turbo",
     stream: true,
     messages: [
       {
         role: "system",
         content:
           "You are a professional chef. You provide detailed cooking instructions, tips, and advice on selecting the best ingredients.",
       },
       ...messages,
     ],
   });
   ```

   > In this code, we added a system message that tells the AI to act as a professional chef, providing detailed cooking instructions, tips, and advice on selecting the best ingredients.

4. Test the app to evaluate how the AI responds to the user's requests

   * Run the app by executing the following command in the terminal:

   ```bash
   npm start
   ```

   * Open the app in your browser and click the 'Random Recipe' button

   * Observe the AI's response

   * Try sending other messages to the AI and observe its responses

   * If the AI's responses are not as expected, you can tweak the code to improve the AI's performance
