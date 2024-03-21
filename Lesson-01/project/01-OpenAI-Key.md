# Setting up your keys

1. Log in to [OpenAI](https://platform.openai.com/)
2. Go to [API Keys](https://platform.openai.com/api-keys)
3. Click on `Create new secret key`
4. Name your key
5. Set permissions to `All`
6. Click on `Create secret key`
7. Copy the key and paste it in an `environment variable` named exactly `OPENAI_API_KEY`:

    ```bash
    # Linux/MacOS/Bash on Windows
    export OPENAI_API_KEY="your-api-key-here"
    ```

    ```bash
    # Windows Command Prompt
    set OPENAI_API_KEY=your-api-key-here
    ```

    ```bash
    # Windows PowerShell
    $env:OPENAI_API_KEY="your-api-key-here"
    ```

8. Check if you have the variable set up correctly by running the following command on your terminal:

    ```bash
    # Linux/MacOS/Bash on Windows
    echo $OPENAI_API_KEY
    ```

    ```bash
    # Windows Command Prompt
    echo %OPENAI_API_KEY%
    ```

    ```bash
    # Windows PowerShell
    echo $env:OPENAI_API_KEY
    ```

9. To check if the key is set up correctly without revealing your key on your terminal, you can display it partially by running the following command:

    ```bash
    # Linux/MacOS/Git Bash on Windows
    echo ${OPENAI_API_KEY:0:3}...
    ```

    ```bash
    # Windows Command Prompt
    echo %OPENAI_API_KEY:~0,3%...
    ```

    ```bash
    # Windows PowerShell
    echo ($env:OPENAI_API_KEY).Substring(0,3) + "..."
    ```

10. Check if you have `sk-...` and not just `...`

>For more instructions on how to complete this in different Operational Systems, go to <https://platform.openai.com/docs/quickstart/step-2-set-up-your-api-key>
