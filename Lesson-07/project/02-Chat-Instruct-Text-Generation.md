# Using Text Generation WebUI to Process Instructions and Chat

1. Load a model fine-tuned for instruction-following tasks

2. Select `Chat` tab

3. Click in the `Show controls` checkbox

4. Scroll down to see the control options

5. Change the mode to `Chat-instruct`

6. Configure the `Command for chat-instruct mode`

   * The `Chat-instruct` mode is useful for managing how each character will behave in the chat by giving specific instructions on how to respond the prompts

   * As an example, let's test if the model can follow instructions to respond in Spanish

   * Put the following command:

   ```text
   Continue the chat dialogue below. Write a single reply for the character "<|character|>".  Always answer in Spanish. Answer in Spanish even when the question is in english.

   <|prompt|>
   ```

7. Type a response in the chat interface and hit `Generate`

   * For example, ask the model `How to make a Pepperoni pizza?`

   * It should now answer in Spanish something like this:

     ```text
     Para hacer una pizza de pepperoni, necesitarás masa para pizza, queso fundido, tomates enlatados, cebollino finamente picado y sal al gusto.

     Empieza calentando el horno a temperatura alta.
     Extiende la masa para pizza en un tablero de cortar.
     Rocíale la base con queso fundido derretido.
     Coloca los tomates enlatados en capas sobre la mezcla de queso.
     Agrega el cebollino finamente picado encima de los tomates.
     Dispón las lonchas de pepperoni por encima del cebollino.
     Esparce sal al gusto.
     Enrolla la pizza hacia arriba.
     Hornea la pizza durante unos 10-12 minutos o hasta que esté dorada y crujiente.
     ```
