import requests
import base64

url = "http://127.0.0.1:7860"

prompt = input("Type your prompt:\n")

payload = {
    "prompt": f"{prompt}, photography, large depth of field, highly detailed, 8k sharp focus, ultra photorealism",
    "negative_prompt": "2D, low quality, text logos, watermarks, signatures, out of frame, jpeg artifacts, ugly, poorly drawn"
}

response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload).json()

# Decode and save the image.
with open("output.png", "wb") as f:
    f.write(base64.b64decode(response["images"][0]))
