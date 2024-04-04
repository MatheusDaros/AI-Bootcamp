# Provide a File in a Thread with a Simple Assistant

1. Using the assistant from the previous exercise, ask the assistant to include `Ahab` and `Moby Dick` in the story

   * Use a prompt like this:

        ```text
        Generate a pirate story including Ahab and Moby Dick
        ```

2. Evaluate how much detail and consistency the assistant provides in the story about these two characters

3. Start a new thread and ask the assistant to generate the same story again from scratch

4. Upload a file with the contents of the book [Moby Dick](./MobyDick.txt) (public domain)

5. Ask the assistant to generate the story again

6. Clone your current assistant and clear the custom instructions

7. Enable the `Retrieval` tool toggle

8. Ask a question that is not present in the training data of this model, but is present in the [Sample Data](./SampleText.txt)

   * Use a prompt like this:

        ```text
        Who is the Captain of the Star-Potato?
        ```

   * The expected output should not contain much information, for example:

        ```text
        I'm not sure what the "Star-Potato" refers to as it doesn't appear to be a real ship or entity. Is it possible that you may be referring to a fictional spaceship or an inside joke? If you can provide more context or details, I'd be happy to try to help.
        ```

9. Upload the [Sample Data](./SampleText.txt) into the chat message

10. Ask the same prompt again

    * The Retrieval function should run and the answer should contain the information provided in the Sample Data and a reference to it

        ```text
        The Captain of the Star-Potato is P1R4T3YOHO123, the most notorious pirate of the cosmos[1].
        ```

11. Try asking something not included in the Sample Data but related to it

    * Use a prompt like this:

        ```text
        What is the biggest weakness of P1R4T3YOHO123?
        ```

    * Some models may not behave well to understand the boundaries of the Sample Data, and the output may contain information not present in the provided data at all

        ```text
        The biggest weakness of P1R4T3YOHO123 is his love for chocolate and his fear of the dark.
        ```
