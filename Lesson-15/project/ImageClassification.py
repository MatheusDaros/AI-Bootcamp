import sys
from PIL import Image
from transformers import pipeline

checkpoint = "openai/clip-vit-large-patch14"
detector = pipeline(model=checkpoint, task="zero-shot-image-classification")

filename = sys.argv[1]
image = Image.open(filename)

labels = input("Enter the labels you want to detect: ").split(" ")

predictions = detector(
    image,
    candidate_labels=labels,
)

i=1
for prediction in predictions:
    label = prediction["label"]
    score = prediction["score"] * 100
    suffix = ''
    if 11 <= (i % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(i % 10, 4)]
    print(f"The word {label} is the {i}{suffix} most related to the image with a confidence of {score:.2f}%")
    i+=1
