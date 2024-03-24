# Using a Local API Chat Completion Tasks

1. Run the Text Generation WebUI application with the API server enabled

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
