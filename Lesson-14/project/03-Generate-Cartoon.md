# Cartoon Image Sequence Generation

1. Reuse the Image Generation python script

2. Load a model suitable for cartoon image generation

3. Configure a prompt for the API to generate four comic images

   * Use `Comic bomb explosion boom, explosion bomb effect, splash, exclamation smoke element, doodle hand drawn text boom, pow, professional cartoon with high details, strong lines, sharp colors, high resolution, masterpiece illustration, professional, ultra hd` as prompt

   * Code the payload to include the prompt and the number of images to be generated

   ```python
   payload = {
       "prompt": "Comic bomb explosion boom, explosion bomb effect, splash, exclamation smoke element, doodle hand drawn text boom, pow, professional cartoon with high details, strong lines, sharp colors, high resolution, masterpiece illustration, professional, ultra hd",
       "n_iter": 4
   }
   ```

   * Use the payload in the API call

4. Loop through the array of images returned by the API and save each image

   ```python
   response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload).json()

   for i in range(4):
       with open(f"bomb_{i+1}.png", "wb") as f:
           f.write(base64.b64decode(response["images"][i]))
   ```

5. Run the script to generate a sequence of cartoon images
