# Generating text with GPTs

1. Start with the Text Generation example `TextGeneration.py` from the Lesson 02

2. Use the following prompt

    ```python
    input_text = "How to make a good sandwich?"
    ```

3. Configure the generation parameters for the model

    ```python
    generated_text = model.generate(**model_inputs, max_length=200, pad_token_id=tokenizer.eos_token_id)
    ```

    >Read more about the `generate` configs at <https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.GenerationConfig>

4. Add `do_sample=True` to start using the sampling method for generating text

   * Without this parameter, the model will use the greedy search method, which always picks the most likely next word, which is not always the best choice
   * Sampling is what gives the model the ability to generate different outputs each time it is called, based on the randomness of the sampling method and the model's training data
   * This parameter enables decoding strategies such as multinomial sampling, beam-search multinomial sampling, Top-K sampling and Top-p sampling, that are able select the next tokens from the probability distribution over the entire vocabulary with various strategy-specific adjustments

5. Add `temperature=0.5` to modulate the probabilities of sequential tokens

   * A temperature of 0.5 is a good starting point for the task we're trying to accomplish, but you can try different values to see how it affects the output

6. Add `top_k=75` to broaden the range of tokens that the model can pick from

   * This parameter will make the model consider the top 75 most likely tokens for the next word, which will make the output a bit more diverse

7. Add `top_p=0.9` to exclude less probable tokens from generation

    * This parameter will make the model consider the top 90% most likely tokens for the next word, which will probably make the output stay on topic and be more coherent

8. Add `repetition_penalty=1.5` to penalize the repetition of tokens in the output

    * This parameter will make the model avoid using the same words and terms over and over again, which will probably make the output more diverse and coherent

9. Run the file

    ```bash
    # Linux/MacOS
    python <filename>.py
    ```

    ```bash
    # Windows
    py <filename>.py
    ```

10. Check the output

    ```text
    How to make a good sandwich?

    Asking this question is like asking how do you build the perfect house. It depends on what kind of person are we talking about, and where they live… You can’t just say “build me one” without knowing more details! So it goes with sandwiches: there isn’t any single recipe that fits all tastes or needs (and if someone tells otherwise – run away). There may be some basic guidelines though which will help us create our own personalized masterpiece from scratch by following these steps below :-) 1) Choose your bread type ;2 ) Pick out fillings according their taste preferences;3.) Assemble everything together nicely before serving up at last step - eating time !!! Enjoy :)
    ```

>Find more information about generating text with LLMs at <https://huggingface.co/docs/transformers/main/en/llm_tutorial#generation-with-llms>
