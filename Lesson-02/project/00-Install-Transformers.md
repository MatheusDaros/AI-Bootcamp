# Installing Hugging Face's Transformers

1. Setup a `Virtual Environment` for the project
   * [Tutorial](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
   * Run `python -m venv .env` (Linux/MacOS) or `py -m venv .venv` (Windows) to create a virtual environment in your project's folder
2. Activate the virtual environment
   * venv [docs](https://docs.python.org/3/library/venv.html)
   * Run `source .env/bin/activate` (Linux/MacOS) or `source .env/Scripts/activate` (Windows) to activate the virtual environment
3. Install the `transformers` package with `pip`
   * pip [docs](https://pip.pypa.io/en/stable/)
   * Run `pip install transformers` to install the `transformers` package
4. Install one of the Machine Learning frameworks compatible with `transformers`
   * Run `pip install 'transformers[torch]'`, `pip install 'transformers[tf-cpu]'` or `pip install 'transformers[flax]'` to install `PyTorch`, `TensorFlow 2.0` or `Flax` respectively
5. Test if your installation was successful
   * Run `python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('I love you'))"` to test if the installation was successful
     * You should get an output similar to this: `[{'label': 'POSITIVE', 'score': 0.9998704791069031}]`
   * Run `python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('I must confess: I have put pineapple on pizza'))"` to test if your model is thinking correctly
     * If you don't get a `NEGATIVE` sentiment from this, your model is definitely not thinking correctly (in my opinion)

>You can check more details about the installation process at <https://huggingface.co/docs/transformers/installation>