# Text Generation WebUI API

1. To enable the API, you need to start the Text Generation WebUI with the `--api` flag

   * Alternatively, you can use the `Session` tab to mark the `api` checkbox in the `Boolean command-line flags` pane

   * The `openai` checkbox must be checked in the `Available extensions` pane for the API to work correctly

2. The API will be available at <http://127.0.0.1:5000>

3. Check the interactive API Documentation at <http://127.0.0.1:5000/docs>

4. The Text Generation WebUI must have a model loaded for the API to be able to handle tasks

5. Check if your API is working correctly by running a test command on the `completions` endpoint

   ```bash
   curl http://127.0.0.1:5000/v1/completions \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "This is a cake recipe:\n\n1.",
       "max_tokens": 200,
       "temperature": 1,
       "top_p": 0.9
     }'
   ```

6. You can now adapt your scripts to consume this local API instead of the OpenAI APIs

   * Use `sseclient-py` to stream data

     * Install it with `pip install sseclient-py`

   * Example of a Python script to consume the local API

     ```python
     import requests
     import sseclient
     import json
     
     url = "http://127.0.0.1:5000/v1/chat/completions"
     
     headers = {
         "Content-Type": "application/json"
     }
     
     history = []
     
     while True:
         user_message = input("> ")
         history.append({"role": "user", "content": user_message})
         data = {
             "mode": "instruct",
             "stream": True,
             "messages": history
         }
     
         stream_response = requests.post(url, headers=headers, json=data, verify=False, stream=True)
         client = sseclient.SSEClient(stream_response)
     
         assistant_message = ''
         for event in client.events():
             payload = json.loads(event.data)
             chunk = payload['choices'][0]['message']['content']
             assistant_message += chunk
             print(chunk, end='')
     
         print()
         history.append({"role": "assistant", "content": assistant_message})
     ```
