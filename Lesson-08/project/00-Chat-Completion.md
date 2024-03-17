# Using a Local API Chat Completion Tasks

1. Install [HttpsProxyAgent](https://www.npmjs.com/package/https-proxy-agent) package to use the local API with the NextJS application

2. Import the `HttpsProxyAgent` package in the `route.ts` file

3. Configure the `httpAgent` when creating the `openai` client

   ```typescript
   const openai = new OpenAI({
      httpAgent: new HttpsProxyAgent(process.env.PROXY_URL),
   });
   ```

4. Now all the API calls will be made through the local API server, and processed by the local GPT model you loaded in the Text Generation WebUI application
