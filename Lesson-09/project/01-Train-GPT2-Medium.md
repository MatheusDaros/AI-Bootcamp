# Training GPT-2 Medium

1. Open Text Generation WebUI

2. Download the GPT-2 Medium model from [OpenAI](https://huggingface.co/openai-community/gpt2-medium)

3. Load the model using the `transformers` loader

4. Put the file to be used for training at the `training/datasets` folder

5. Open the `Training` tab

6. In the right pane, select the `Raw text file` tab

   * Hit the refresh button to populate the list of files in the dropdown

   * Select your file from the dropdown

7. Set the training parameters in the left pane

   * Fill a name for the new LoRA file

   * Set the `LoRA Rank` to `512` and `LoRA Alpha` to `1024`

   * Increase the `Batch Size` to `1024`

     * If you get an out-of-memory error, reduce the batch by half until the training works in your device

   * Increase `Epochs` to `10`

     * This might take a long time depending on your configurations, so you can start with a lower number and increase it later

     * If you place it too low, it might not reach the desired convergence we want

   * Set `Learning Rate` to `1e-3`

8. Change the `LR Scheduler` options to control convergence

   * Use `1.2` as the `Stop at loss` parameter

9. Hit the `Start LoRA Training` button and wait for the training to finish

   * Remember to reload the model after the training is finished

10. Before activating the LoRA, test the model with a simple completion

    * In the `Parameters` tab, set the `Max tokens` to `20` and `temperature` to `0.5`

    * In the `Notebook` tab, complete a simple prompt (for example, `To be or not to`)

    * Hit the `Generate` and `Regenerate` buttons a few times to sample the model's output

    * Evaluate the `Logits` tab to see the probabilities of each token to be suggested next

      * Input `To be or not to` text in the `Output` tab and click in the `Generate next token probabilities` button

11. Activate the LoRA

    * In the `Model` tab, select your LoRA from the dropdown

      * You might need to hit the refresh button to populate the list of LoRAs

    * Click on `Apply LoRAs`

12. Test the model again

    * In the `Notebook` tab, complete a simple prompt (for example, `To be or not to`)

    * Hit the `Generate` and `Regenerate` buttons a few times to sample the model's output

    * Evaluate the `Logits` tab to see the probabilities of each token to be suggested next

      * Input `To be or not to` text in the `Output` tab and click in the `Generate next token probabilities` button
