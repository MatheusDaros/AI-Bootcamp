import torch
from diffusers import DiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"

pipeline = DiffusionPipeline.from_pretrained(model_id, use_safetensors=True)

pipeline = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True).to("cuda")

generator = torch.Generator("cuda").manual_seed(0)

prompt = "A picture of a Pepperoni Pizza in a restaurant table"

image = pipeline(prompt, generator=generator).images[0]
image.save("output.png")