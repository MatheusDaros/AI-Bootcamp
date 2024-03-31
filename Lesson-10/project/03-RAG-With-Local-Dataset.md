# Using RAG in the Text Generation WebUI

1. Setup the `superbooga` extension in Text Generation Web UI

   * Activate [Superbooga](https://github.com/oobabooga/text-generation-webui/tree/main/extensions/superbooga) in the `Session` tab

   * Terminate the current session

   * Activate the `conda` environment in the `installer_files/env` folder

   * Navigate to the `extensions/superbooga` folder

   * Run `pip install -r requirements.txt`

   * Deactivate the `conda` environment with `conda deactivate`

   * Restart the Text Generation Web UI and activate the `superbooga` extension

   * Click on `Apply flags/extensions and restart` to load the extension

2. Select a model in the `Model` tab

   * Choose a model that is trained for instruction-following tasks

     * For example [AWQ version of Vicuna 7B v1.5](https://huggingface.co/TheBloke/vicuna-7B-v1.5-AWQ)

3. Open the `Notebook` tab

4. Input the following prompt in the `Textbox`:

   ```text
   <|begin-user-input|>
   What is this story about?
   <|end-user-input|>
   
   <|injection-point|>
   
   ASSISTANT:
   ```

5. Hit `Generate` to generate the response

   * The `<|injection-point|>` will be empty, since we haven't loaded any data yet

   * The generated response should be a generic hallucination from the model or something similar

6. Scroll down to see the `File input` tab and upload the [Sample Data](./SampleText.txt) to it

   * Configure `\n` as the `Chunk separator` to split the file into paragraphs

7. Click on `Load data` to add the _chunks_ to the database

8. Test the prompt again

   * The response should now contain information from the Sample Data

   * Each chunk in the database will be compared to the current input, and the most relevant matches will be appended to the input before starting the inference process

     * You can configure the amount of context to be appended by changing the `Chunk count` value

       * For example, you can set it to `1` to append only the single most relevant chunk pertaining to the current input

9. You may also test the RAG functionalities in the `Chat` tab

   * This only works in the `instruct` mode

   * In the `chat` mode, the extension will work to keep an extended context with the history of the conversation

     * At each new message, the most relevant past messages will be appended to the context string, and the extension will ignore the external data sources
