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

## Create Your Next.js Project

1. Create your project:

   ```bash
   npx create-next-app my-ai-app
   ```

2. Choose all default options.

3. Navigate to the created folder:

   ```bash
   cd my-ai-app
   ```

4. Open the `global.css` file and import these modules at the top of the page:

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

5. Open the `pages/index.tsx` file.

6. At the top of the file, import the `useState` hook:

   ```javascript
   import { useState } from "react";
   ```

7. Define the initial state of the variables we'll be using:

   ```javascript
   function Home() {
     const [messageHistory, setmessageHistory] = useState([""]);
     const [inputValue, setInputValue] = useState("");
     const [isLoading, setIsLoading] = useState(false);
     const [prompt, setPrompt] = useState([{}]);
   }
   ```

8. Write a function that updates the input value as the user types and updates the messages state accordingly:

   ```javascript
   const handleInputChange = (e) => {
     setInputValue(e.target.value);
     setMessages([
       {
         role: "system",
         content: "Tell a story according to what the user has said to you",
       },
       { role: "user", content: e.target.value },
     ]);
   };
   ```

9. Write a function to generate text that will handle sending the user's message to the text generation webUI server:

   ```javascript
   const generateText = async () => {
     setIsLoading(true);
     setInputValue("");
     const response = await fetch("http://127.0.0.1:5000/v1/chat/completions", {
       method: "POST",
       headers: {
         "Content-Type": "application/json",
       },
       body: JSON.stringify({ prompt }),
     });
     const data = await response.json();
     console.log(prompt);
     const newContent = data.choices[0].message.content;
     setmessageHistory((prevmessageHistory) => [
       ...prevmessageHistory,
       newContent,
     ]);
     setIsLoading(false);
   };
   ```

10. Return the JSX structure for the Home component:

    ```javascript
    return (
      <div>
        {/* History display */}
        {/* Loading indicator */}
        {/* Input field and button */}
      </div>
    );
    ```

11. Inside the returned JSX, use a map method to iterate through `messageHistory` and display each message:

    ```javascript
    return (
      <div>
        <div className="px-10">
          {history.map((content, index) => (
            <div className="py-5" key={index}>
              {content}
            </div>
          ))}
        </div>
        {/* Loading indicator */}
        {/* Input field and button */}
      </div>
    );
    ```

12. Add an input field and a button for user interaction:

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

13. Conditionally render a loading indicator if `isLoading` is true above the button:

    ```javascript
    {
      isLoading && <p className="flex justify-center pt-5">Loading...</p>;
    }
    ```

14. If you followed all the steps correctly, your component should look like this:

    ```javascript
    "use client";

    import { useState } from "react";

    export default function Home() {
      const [messageHistory, setmessageHistory] = useState([""]);
      const [inputValue, setInputValue] = useState("");
      const [isLoading, setIsLoading] = useState(false);
      const [prompt, setPrompt] = useState([{}]);

      const handleInputChange = (e: any) => {
        setInputValue(e.target.value);
        setPrompt([
          {
            role: "system",
            content: "Tell a story according to the what the user has said to you",
          },
          { role: "user", content: e.target.value },
        ]);
      };

      const generateText = async () => {
        setIsLoading(true);
        setInputValue("");
        const response = await fetch("http://127.0.0.1:5000/v1/chat/completions", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ prompt }),
        });
        const data = await response.json();
        console.log(prompt);
        const newContent
    ```

15. Now all that's left is for you to test how the AI will continue the story depending on what you say to it.
