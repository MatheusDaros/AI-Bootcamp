import requests
import base64

url = "http://127.0.0.1:7860"

payload = {
    "prompt": input("What would you like to generate?\n"),
    "negative_prompt": input("What would you like to avoid in the image?\n"),
    "steps": int(input("How many steps would you like to take?\n"))
}

response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload).json()

with open("output.png", 'wb') as f:
    f.write(base64.b64decode(response['images'][0]))