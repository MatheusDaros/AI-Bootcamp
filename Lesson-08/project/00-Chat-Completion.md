# Using a Local API Chat Completion Tasks

1. Run the Text Generation WebUI application with the API server enabled

   >As of **27th of March of 2024**, the `main` branch of the Text Generation WebUI application have a bug in the `chat` endpoint, documented [in this issue](https://github.com/oobabooga/text-generation-webui/issues/5761)
   >>The fix has been developed in [this PR](https://github.com/oobabooga/text-generation-webui/pull/5722) and has been merged in the `dev` branch
   >>>Currently, to use the `chat` endpoint, you must use the `dev` branch of the Text Generation WebUI application by running `git checkout dev` after cloning and doing a clean install of the project
   >>>>Or you can apply the fix manually by editing the `extensions/openai/typing.py` file and changing the line `110` to `user_bio: str | None = Field(default='', description="The user description/personality.")`

2. Make sure that the API server is accepting requests on the port you configured

   * Check also if you have loaded a model in the Text Generation WebUI application

3. Configure the `baseURL` parameter of OpenAI client

   ```typescript
   const openai = new OpenAI({
      baseURL: `http://127.0.0.1:5000/v1`,
   });
   ```

   * If you configured the API server to run on a different port, you must change the `5000` to the port you have configured

4. Now all the API calls will be made through the local API server, and processed by the local GPT model you loaded in the Text Generation WebUI application
