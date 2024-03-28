import requests
import base64

url = "http://127.0.0.1:7860"


for i in range(4):
    payload = {
        "prompt": "Comic bomb boom. Hand drawn cartoon explosion bomb effect, splash, exclamation smoke element. Doodle hand drawn text boom, pow"
    }

    response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload)
    r = response.json()

    # Decode and save the image.
    with open(f"bomb_{i+1}.png", "wb") as f:
        f.write(base64.b64decode(r["images"][0]))
