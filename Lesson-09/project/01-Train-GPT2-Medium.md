# Training GPT-2 Medium

1. Create an account at [Google Colab](colab.research.google.com)

   * Unless you have access to a good cluster of GPUs, training even the most basic GPT-2 model can be very time consuming and expensive

   * Google Colab offers free access to GPUs and TPUs, which can be used to train GPT-2 models

2. Access the [Collaborative notebook](https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce)

3. Log in with your account

4. Follow the steps in the notebook to train a GPT-2 model with the sample data provided

   * Pick the medium model (`355M`) for this exercise

   * Upload a new sample text file to train the model

   * Use the sample data (`"new-sample.txt"`) in the notebook to train the model

5. Fine-tune the model until it reaches a `loss` under `2.0`

6. Generate some text from the new pre-trained model
