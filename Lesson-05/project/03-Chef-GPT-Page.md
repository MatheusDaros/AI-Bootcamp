# Building the Chef GPT App

In this exercise, we will enhance our chat application to function as a virtual chef. Here's a step-by-step guide:

1. Open the 'page.tsx' file

2. First, set the chat container's height to 100% of the screen by adding "h-screen" to the outer div. This prevents new elements from overlapping:

```typescript
 <div className="flex flex-col w-full h-screen max-w-md py-24 mx-auto stretch">
```

3. Next, wrap the chat messages in a div container to manage overflow, height, and scrolling as messages are generated:

```typescript
<div className="overflow-auto h-[88%] w-full">
  {messages.map((m) => (
    <div key={m.id} className="whitespace-pre-wrap">
      {m.role === "user" ? "User: " : "AI: "}
      {m.content}
    </div>
  ))}
</div>
```

4. Extract `append` and `isLoading` from the [useChat hook]('https://sdk.vercel.ai/docs/api-reference/use-chat') provided by Vercel AI SDK. We'll use these in the upcoming steps:

```typescript
const { messages, input, handleInputChange, handleSubmit, isLoading, append } = useChat();
```

5. Next, use `isLoading` to decide if a loading element should be displayed while messages are being generated. Add this code inside the div that we created to contain the chat messages in step 3:

```typescript
{
  isLoading && (
    <div className="flex justify-end pr-4">
      <span className="animate-bounce">...</span>
    </div>
  )
}
```

6. Next, add styles to give the messages a chat bubble appearance. Update the messages element with the following code:

```typescript
{
  messages.map((m) => (
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
  ))
}
```

7. If you followed the steps until now, the code should look like this:

```typescript
"use client";

import { useChat } from "ai/react";

export default function Chat() {
  const {
    messages,
    input,
    handleInputChange,
    handleSubmit,
    isLoading,
    append,
  } = useChat();
  return (
    <div className="flex flex-col w-full h-screen max-w-md py-24 mx-auto stretch">
      <div className="overflow-auto h-[88%] w-full">
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

8. At this point, the page looks good. However, when there are many messages, the user must manually scroll to see new messages. Let's address this by adding automatic scrolling:

  * Import useEffect and useRef from the 'react' package at the top of the code (after "useChat" import). These are two functions from React that allow us to, respectively, perform side effects in functional components and access the properties of a DOM element:

`import { useEffect, useRef } from "react";`
  
  * Create a reference for the messages container and scroll the page when new messages appear:

```typescript
  const messagesContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [messages]);
```

  * Attach the reference to the messages container created in step 3:

```typescript
 <div className="overflow-auto h-[88%] w-full" ref={messagesContainerRef}>
```

9. Let's further customize the page by adding a button that prompts the AI to return a random recipe:

  * First, create a container at the bottom of our page. Do this by wrapping our form with a div and moving some classes from the form to the div container:

```typescript
<div className="fixed bottom-0 w-full max-w-md">
  <form onSubmit={handleSubmit}>
    <input
      className="w-[95%] p-2 mb-8 border border-gray-300 rounded shadow-xl text-black"
      value={input}
      placeholder="Say something..."
      onChange={handleInputChange}
    />
  </form>
</div>
```

  * Next, add a button inside the container we just created to request a random recipe. Use the `append` function from the `useChat` hook, which we extracted in step 4. Call this function when the user clicks the button with the following code:

```typescript
<div className="flex flex-col justify-center items-center">
  <button
    className="bg-blue-500 p-2 text-white rounded shadow-xl"
    disabled={isLoading}
    onClick={() => append({ role: "user", content: "Give me a random recipe" })}
  >
    Random Recipe
  </button>
  <p className="p-4">OR</p>
</div>
```

  * We can use the same `isLoading` value from step 5 to disable the button and the input. This prevents the user from sending multiple clicks or messages while a response is being generated. The final code should look like this:

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

  const messagesContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (messagesContainerRef.current) {
      messagesContainerRef.current.scrollTop =
        messagesContainerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div className="flex flex-col w-full h-screen max-w-md py-24 mx-auto stretch">
      <div className="overflow-auto h-[88%] w-full" ref={messagesContainerRef}>
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
        <div className="flex flex-col justify-center items-center">
          <button
            className="bg-blue-500 p-2 text-white rounded shadow-xl"
            disabled={isLoading}
            onClick={() =>
              append({ role: "user", content: "Give me a random recipe" })
            }
          >
            Random Recipe
          </button>
          <p className="p-4">OR</p>
        </div>
        <form onSubmit={handleSubmit} className="flex justify-center">
          <input
            className="w-[95%] p-2 mb-8 border border-gray-300 rounded shadow-xl text-black"
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

10. Last but not least. Set up the AI to act as a chef

   * Now, let's make the AI act like a chef

   * Replace the code that creates chat completions in the 'route.tsx' file inside the 'src/app/api/chat' folder:

   ```typescript
   // rest of the code

export async function POST(req: Request) {
  const { messages } = await req.json();
 
  // Ask OpenAI for a streaming chat completion given the prompt
  const response = await openai.chat.completions.create({
    model: 'gpt-3.5-turbo',
    stream: true,
    messages: [
      {
        role: 'system',
        content: 'You are a professional chef. You provide detailed cooking instructions, tips, and advice on selecting the best ingredients.',
      },
      ...messages,
    ],
  });
 
  // Convert the response into a friendly text-stream
  const stream = OpenAIStream(response);
  // Respond with the stream
  return new StreamingTextResponse(stream);
}
   ```

   > In this code, we added a system message that tells the AI to act as a professional chef, providing detailed cooking instructions, tips, and advice on selecting the best ingredients.

11. Test the app to evaluate how the AI responds to the user's requests

   * Run the app by executing the following command in the terminal:

   ```bash
   npm run dev
   ```

   * Open the app in your browser at http://localhost:3000/ and click the 'Random Recipe' button

   * Observe the AI's response

   * Try sending other messages to the AI and observe its responses

   * If the AI's responses are not as expected, you can tweak the code to improve the AI's performance
