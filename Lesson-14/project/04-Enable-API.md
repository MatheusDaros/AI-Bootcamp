# Enabling the API in Stable Diffusion WebUI

1. Enable the `--api` flag

   * Edit the `webui-user.bat` (Windows) or `webui-user.sh` (Linux/mac) file

   * Locate the `#export COMMANDLINE_ARGS=""` line

   * Remove the comment `#` and add the `--api` flag

     * Linux/MacOS

     ```bash
     export COMMANDLINE_ARGS="--api"
     ```

     * Windows

     ```bash
     set COMMANDLINE_ARGS="--api"
     ```

2. Save the file and restart the Diffusion WebUI

   * You should see a message saying `Launching Web UI with arguments: --api` when the WebUI starts

3. Access the API Swagger interface

   * Open a web browser and navigate to `http://127.0.0.1:7860/docs`

   * You should see the Swagger UI interface with all the available API endpoints

4. Test the API

   * Run a test with the `sdapi/v1/txt2img` endpoint by passing the following payload

     ```json
     {
         "prompt": "a dog playing with a red rubber ball"
     }
     ```

   * The API should return a response with the image generated from the prompt under the `images` key

     * You can use any [online converter](https://base64.guru/converter/decode/image) to decode the base64 image string to view the image
