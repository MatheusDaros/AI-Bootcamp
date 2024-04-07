import sys
from transformers import pipeline
from PIL import Image, ImageDraw

checkpoint = "google/owlv2-base-patch16-ensemble"
detector = pipeline(model=checkpoint, task="zero-shot-object-detection")

filename = sys.argv[1]
image = Image.open(filename)

labels = input("Enter the labels you want to detect: ").split(" ")

predictions = detector(
    image,
    candidate_labels=labels,
)

draw = ImageDraw.Draw(image)
for prediction in predictions:
    box = prediction["box"]
    label = prediction["label"]
    score = prediction["score"]

    xmin, ymin, xmax, ymax = box.values()
    draw.rectangle((xmin, ymin, xmax, ymax), outline="red", width=1)
    draw.text((xmin, ymin), f"{label}: {round(score,2)}", fill="black")

image.save(f"{filename.split('.')[0]}_detection.png")