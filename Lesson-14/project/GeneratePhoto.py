import requests
import base64

# Define the URL and the payload to send.
url = "http://127.0.0.1:7860"

prompt = input("Type your prompt:\n")

payload = {
    "prompt": f"{prompt}, shot 35 mm, realism, octane render, 8k, trending on artstation, 35 mm camera, unreal engine, hyper detailed, photo - realistic maximum detail, volumetric light, realistic matte painting, hyper photorealistic, trending on artstation, ultra - detailed, realistic"
}

# Send said payload to said URL through the API.
response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload)
r = response.json()

# Decode and save the image.
with open("output.png", "wb") as f:
    f.write(base64.b64decode(r["images"][0]))
