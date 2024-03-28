# Building a prompt to generate stories

1. Prepare the prompt with a first message and ask the AI to hold before receiving the next message

   * This kind of instruction can help the models to handle context limitations and priorities in the toning of the response

   * Again, this is another technique that relies on the fine-tuning of the model for instructions

2. Pass the initial prompt

   * Examples:

     ```text
     As a professional storyteller, write a prompt to tell engaging stories about a theme that the user will provide in the next message. The stories should be engaging, entertaining, and inspiring. They should include a mix of humor, drama, and suspense to captivate the audience. Use vivid descriptions and relatable characters to bring the stories to life. The user will provide the theme in the next message. Answer this message with "OK" only.
     ```

     ```text
     You are a professional storyteller who has been hired to write a series of short stories for a new anthology. The stories should be captivating, imaginative, and thought-provoking. They should explore a variety of themes and genres, from science fiction and fantasy to mystery and romance. Each story should be unique and memorable, with compelling characters and unexpected plot twists. The user will provide the theme for the first story in the next message. Answer this message with "OK" only.
     ```

3. Check if the model responded correctly with just `"OK"`

4. Pass the theme for the story to be generated

   * Considerations:

     * Since generating fictional stories doesn't require any sort of factual accuracy with the real world, the _loose link_ that the models have with the constrains and rules of the real world can be a good thing for this kind of task, since eventual hallucinations or misinterpretations of the prompt can lead to very interesting and creative stories, and not to misinformation or disinformation about the real world

     * Models can be fine-tuned to double-down in this effect to generate some sort of "parallel reality", where most of the things resemble the world as it is (based in the training data of the model), but eventually some things might come out completely different

     * This possible silver lining about the limitations of the models needs to be carefully balanced, since it can easily cause a consistency problem in the story being generated

       * For example, if the model hallucinated in a point of the story by (incorrectly) stating that bananas are blue, but then later on (correctly) refer to bananas as yellow, it can create tears in the narrative, spoiling the quality of the story

         * This problem is not trivial to solve, since it requires maintaining each single borderline irrelevant fact in the context while still being able to efficiently recall about it and consider it with maximum respect the next time the subject arises (even when conflicting over the very training data of the model)

5. Evaluate the quality of the output
