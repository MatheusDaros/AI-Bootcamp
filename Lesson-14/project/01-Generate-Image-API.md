# Generating images with the Stable Diffusion WebUI API

1. Make sure the API is running at <http://127.0.0.1:7860/docs>

2. Create a new Python script, open it in your favorite editor, and add the code to generate a image by calling the API

   * Start with the following code:

   ```python
   import requests
   import base64

   url = "http://127.0.0.1:7860"
   ```

3. Prepare the input from the user

   ```python
   payload = {
       "prompt": input("What would you like to generate?\n"),
       "negative_prompt": input("What would you like to avoid in the image?\n"),
       "steps": int(input("How many steps would you like to take?\n"))
   }
   ```

4. Make a request to the API

   ```python
   response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload).json()
   ```

5. Decode the image from the response

   ```python
   with open("output.png", 'wb') as f:
       f.write(base64.b64decode(response['images'][0]))
   ```

6. Run the script and check the output

   ```bash
   python generate_image.py
   ```

   * You should see a new image file named `output.png` in the same directory as the script
