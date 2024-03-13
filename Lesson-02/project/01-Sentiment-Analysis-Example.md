# Running a Sentiment Analysis pipeline example

1. Create a new Python file
   * Create a new file in your favorite code editor or simply run `touch <filename>.py` in your terminal (Linux/MacOS) or `type nul > <filename>.py` in your terminal (Windows)
     * Remember to replace `<filename>` with the name of your file
2. Import the `pipeline` module from the `transformers` package
   * Add the following line to your file using your favorite code editor:

    ```python
    from transformers import pipeline
    ```

3. Create a new instance of the Text Classification Pipeline in a variable

    ```python
    classifier = pipeline('sentiment-analysis')
    ```

4. Create a new variable to store the text to be analyzed

    ```python
    text = "I love coding in python!"
    ```

5. Run the `classifier` pipeline with the `text` variable as input

    ```python
    result = classifier(text)[0]
    ```

6. Format and print the result

    ```python
    print(f"The text \"{text}\" was classified as {result['label']} with a score of {round(result['score'], 4) * 100}%")
    ```

7. Run the file

    ```bash
    # Linux/MacOS
    python <filename>.py
    ```

    ```bash
    # Windows
    py <filename>.py
    ```

8. The warnings can be ignored, since the default models loaded are good enough for this tutorial

9. The result should be similar to: `The text "I love coding in python!" was classified as POSITIVE with a score of 99.91%`

10. Modify the script to accept the text as a parameter

    ```python
    from transformers import pipeline
    import sys

    classifier = pipeline('sentiment-analysis')

    text = sys.argv[1]

    result = classifier(text)[0]

    print(f"The text \"{text}\" was classified as {result['label']} with a score of {round(result['score'], 4) * 100}%")
    ```

11. Run the file with a text as a parameter

    ```bash
    # Linux/MacOS
    python <filename>.py "Python is awesome, but whitespace is awful"
    ```

    ```bash
    # Windows
    py <filename>.py "I prefer Bython over Python"
    ```

12. The result should be similar to: `The text "Python is awesome, but whitespace is awful" was classified as NEGATIVE with a score of 98.64%`

>For more information about the `Text Classification` pipeline, check <https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextClassificationPipeline>
