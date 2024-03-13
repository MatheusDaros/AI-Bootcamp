# Generating text with LLMs

1. Install all of the required dependencies for this exercise
   * Run `pip install bitsandbytes auto-gptq optimum`
2. Create a new Python file
   * Create a new file in your favorite code editor or simply run `touch <filename>.py` in your terminal (Linux/MacOS) or `type nul > <filename>.py` in your terminal (Windows)
     * Remember to replace `<filename>` with the name of your file
3. Import the `AutoModelForCausalLM`, `BitsAndBytesConfig`, and `AutoTokenizer` modules from the `transformers` package
   * Add the following line to your file using your favorite code editor:

    ```python
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    ```

4. Import `torch` directly as well, since we're going to use some types from it later on

    ```python
    import torch
    ```

5. Create a new instance of the Tokenizer in a variable to process the text inputs and also to decode generated outputs later on
   * We're going to use the `AutoTokenizer` class to automatically download the tokenizer suitable for the model we're using

    ```python
     tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1", padding_side="left")
    ```

6. Create a quantization configuration object to use with the model
   * We're going to use the `QuantizationConfig` class to configure the quantization of the model

    ```python
    quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)
    ```

   * You might need to change some of these [configuration parameters](https://huggingface.co/docs/transformers/main_classes/quantization#transformers.BitsAndBytesConfig) to better fit your hardware and the model you're using

7. Create a new instance of the LLM model in a variable using a `pre-trained model call` function
   * We're going to use the `mistralai/Mistral-7B-v0.1` model, that will be automatically downloaded from the Hugging Face's model hub
   * We're going to use [4-bit dynamic quantization](https://huggingface.co/docs/transformers/main/en/main_classes/quantization) to make the model run faster and use less memory, while sacrificing a little bit of accuracy
   * You can run with the `device_map="auto"` option to use more of your GPU(s) if you have one or many available in your device

    ```python
    model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1", quantization_config=quantization_config, device_map="auto", low_cpu_mem_usage=True)
    ```

8. Use the Tokenizer to encode the input text and store the result in a variable

    ```python
    input_text = "What is the best recipe for Pepperoni pizza?"
    model_inputs = tokenizer([input_text], return_tensors="pt").to("cuda")
    ```

9. Generate text using the model and the tokenized input text

    ```python
    generated_text = model.generate(**model_inputs, max_length=20, pad_token_id=tokenizer.eos_token_id)
    ```

10. Decode the generated text and print the result

    ```python
    result = tokenizer.batch_decode(generated_text, skip_special_tokens=True)[0]
    print(result)
    ```

11. Run the file

    ```bash
    # Linux/MacOS
    python <filename>.py
    ```

    ```bash
    # Windows
    py <filename>.py
    ```

12. Expect a considerable load time if you're running this command for the first time, as the `mistralai/Mistral-7B-v0.1` model will be downloaded from the Hugging Face's model hub

    * The model is almost 15GB in size, so make sure you have enough disk space available in your device and a stable internet connection
    * The model will be downloaded to the `~/.cache/huggingface/transformers` directory in your device and will be available for future runs of the same script without downloading it again

13. If you get an "Out Of Memory" error, try to tweak the quantization parameters to make the computation fit in your device's memory
    * If all else fails, you can also try to run the script in a cloud-based environment with more resources available

14. If your script ran correctly, you should get an output like this:

    ```bash
    What is the best recipe for Pepperoni pizza?
    - Directions Preheat oven to 425 degrees F (220 degrees C). In a large bowl, combine the pizza sauce, pepperoni, and mozzarella cheese. Spread the mixture over the pizza crust. Bake in the preheated oven for 10 to 15minutes, or until the cheese is melted and the crust is lightly browned.
    
    ```

>Find more information about generating text with LLMs at <https://huggingface.co/docs/transformers/main/en/llm_tutorial#generation-with-llms>