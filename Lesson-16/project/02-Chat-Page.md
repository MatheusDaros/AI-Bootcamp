# Adding a page to chat with a text generation model

## Install Text Generation WebUI

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/oobabooga/text-generation-webui.git
   ```

2. Change to the `text-generation-webui` directory:

   ```bash
   cd text-generation-webui
   ```

3. Run the installation script:

   - Use `start_linux.sh` script for Linux

   ```bash
   ./start_linux.sh
   ```

   - Use `start_windows.bat` script for Windows in cmd

   ```bash
   start_windows.bat
   ```

   - Use `start_macos.sh` script for MacOS

   ```bash
   ./start_macos.sh
   ```

   - Use `start_wsl.bat` script for Windows Subsystem for Linux

   ```bash
   start_wsl.bat
   ```

4. Wait for the download and installation of dependencies to finish.

5. When prompted, select your GPU manufacturer and model.

   - If you don't have a GPU, select `N` to run the models in CPU mode.

6. Confirm the selection and wait until the entire installation process finishes.

   - Look for a message saying `Successfully installed ...` at the end of the installation process.

   - If this is your first time installing the repository, you should also see:

   ```text
   *******************************************************************
   * You haven't downloaded any model yet.
   * Once the web UI launches, head over to the "Model" tab and download one.
   *******************************************************************
   ```

   - The last message in your terminal should be:

   ```text
   Running on local URL:  http://127.0.0.1:7860
   ```

7. Open your browser and go to <http://localhost:7860> to test if the application is working.

8. Click on the "Session" tab on the navbar and check the API flag.

9. Click on the "apply flags/extensions and restart" button.

10. The API is now running on the http://127.0.0.1:5000/v1/completions endpoint.

11. Create a new folder to hold our page layout and our logic.

- In the root of your project, find the `app` folder and create a new folder inside it named `text-generation`.

- Inside the `text-generation` folder create a `page.tsx` file and access it.

12. At the top of the file, import the `useState` hook:

```javascript
import { useState } from "react";
```

13. Define the initial state of the variables we'll be using:

- Messages will be useful keep track of the conversation messages. It's an array of objects where each object represents a message in the conversation.

- inputValue is a state variable that holds the current value of the input field where the user can type their message to continue the conversation.

- isLoading controls whether a loading indicator should be displayed.

```javascript
export default function Home() {
  const [messages, setMessages] = useState([
    {
      role: "system",
      content: "Craft a narrative based on the user's input",
    },
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
}
```

14. Write a function that updates the input value to whatever the user has typed in:

```javascript
const handleInputChange = (e: any) => {
  setInputValue(e.target.value);
};
```

15. Write a function that will handle sending the user's message to the text generation webUI server:

```javascript
const generateText = async () => {
  setIsLoading(true);
  setInputValue("");
  setMessages((prevMessages) => [
    ...prevMessages,
    { role: "user", content: inputValue },
  ]);
  const userQueryData = [...messages, { role: "user", content: inputValue }];
  const response = await fetch("http://127.0.0.1:5000/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ messages: userQueryData }),
  });
  const data = await response.json();
  const newContent = data.choices[0].message.content;
  setMessages((prevMessages) => [
    ...prevMessages,
    { role: "assistant", content: newContent },
  ]);
  setIsLoading(false);
};
```

16. Return the JSX structure for the Home component:

    ```javascript
    return (
      <div>
        {/* History display */}
        {/* Loading indicator */}
        {/* Input field and button */}
      </div>
    );
    ```

17. Inside the returned JSX, use a map method to iterate through the `messages` and display each message:

    ```javascript
    return (
    <div>
      <div className="px-10">
        {messages.map(({ content, role }, index) =>
          index > 0 ? (
            <div className="py-5 mx-auto" key={index}>
              <p className="font-bold">{role === "user" ? "You" : "AI"}</p>
              <p> {content}</p>
            </div>
          ) : null
        )}
      </div>
    )
    ```

18. Add an input field and a button for user interaction:

    ```javascript
    <div className="py-5 flex justify-center">
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        className="bg-gray-100 p-2 mr-2 rounded shadow"
        placeholder="Continue the story"
      />
      <button
        disabled={!inputValue || isLoading}
        className="bg-blue-500 p-2 text-white rounded shadow-xl disabled:bg-blue-500/20"
        onClick={generateText}
      >
        Send
      </button>
    </div>
    ```

19. Conditionally render a loading indicator if `isLoading` is true above the button added in the previous step:

    ```javascript
    {
      isLoading && <p className="flex justify-center pt-5">Loading...</p>;
    }
    ```

20. If you followed all the steps correctly, your component should look like this:

```javascript
"use client";

import { useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState([
    {
      role: "system",
      content: "Craft a narrative based on the user's input",
    },
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (e: any) => {
    setInputValue(e.target.value);
  };

  const generateText = async () => {
    setIsLoading(true);
    setInputValue("");
    setMessages((prevMessages) => [
      ...prevMessages,
      { role: "user", content: inputValue },
    ]);
    const userQueryData = [...messages, { role: "user", content: inputValue }];
    const response = await fetch("http://127.0.0.1:5000/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ messages: userQueryData }),
    });
    const data = await response.json();
    const newContent = data.choices[0].message.content;
    setMessages((prevMessages) => [
      ...prevMessages,
      { role: "assistant", content: newContent },
    ]);
    setIsLoading(false);
  };

  return (
    <div>
      <div className="px-10">
        {messages.map(({ content, role }, index) =>
          index > 0 ? (
            <div className="py-5 mx-auto" key={index}>
              <p className="font-bold">{role === "user" ? "You" : "AI"}</p>
              <p> {content}</p>
            </div>
          ) : null
        )}
      </div>
      {isLoading && <p className="flex justify-center pt-5">Loading...</p>}
      <div className="py-5 flex justify-center">
        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          className="bg-gray-100 p-2 mr-2 rounded shadow"
          placeholder="Continue the story"
        />
        <button
          disabled={!inputValue || isLoading}
          className="bg-blue-500 p-2 text-white rounded shadow-xl disabled:bg-blue-500/20"
          onClick={generateText}
        >
          Send
        </button>
      </div>
    </div>
  );
}
```

21. Now all that's left is for you to test how the AI will continue the story depending on what you say to it.
