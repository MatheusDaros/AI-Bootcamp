from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
  image=open("Coconut.png", "rb"),
  n=1,
  size="1024x1024"
)

print(f"Variation: {response.data[0].url}")

response = client.images.edit(
  model="dall-e-2",
  image=open("Coconut.png", "rb"),
  mask=open("Mask.png", "rb"),
  prompt="A football ball in the beach",
  n=1,
  size="1024x1024"
)

print(f"Edit: {response.data[0].url}")