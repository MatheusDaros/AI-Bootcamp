import requests
import base64

url = "http://127.0.0.1:7860"

payload = {
    "prompt": "Comic bomb explosion boom, explosion bomb effect, splash, exclamation smoke element, doodle hand drawn text boom, pow, professional cartoon with high details, strong lines, sharp colors, high resolution, masterpiece illustration, professional, ultra hd",
    "n_iter": 4
}

response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload).json()

for i in range(4):
    with open(f"bomb_{i+1}.png", "wb") as f:
        f.write(base64.b64decode(response["images"][i]))
