# Running a Zero-shot Image Classification Pipeline

1. Load the `venv` environment where you have installed `transformers` in previous lessons

2. Create a python file named `ImageClassification.py`

3. Import the needed libraries

   ```python
   import sys
   from PIL import Image
   from transformers import pipeline
   ```

4. Import the model and define the pipeline

   ```python
   checkpoint = "openai/clip-vit-large-patch14"
   detector = pipeline(model=checkpoint, task="zero-shot-image-classification")
   ```

5. Load the image passed as argument to the script

   ```python
   filename = sys.argv[1]
   image = Image.open(filename)
   ```

6. Receive the list of objects to detect as user input

   ```python
   labels = input("Enter the labels you want to detect: ").split(" ")
   ```

   * The list of words must be separated by single spaces

7. Run the pipeline and get the results

   ```python
    predictions = detector(
        image,
        candidate_labels=labels,
    )
   ```

8. Print the probabilities for each word

   ```python
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
   ```

9. Run the script with the image file

   ```bash
   python ImageClassification.py CowChicken.png
   #Enter the labels you want to detect: Animals Humans Machines Buildings
   ```

   * Example output:

     ```bash
     The word Animals is the 1st most related to the image with a confidence of 98.90%
     The word Machines is the 2nd most related to the image with a confidence of 0.72%
     The word Humans is the 3rd most related to the image with a confidence of 0.32%
     The word Buildings is the 4th most related to the image with a confidence of 0.07%
      ```
