# Building a prompt to fact-check statements

1. Prepare the prompt with a fist message and ask the AI to hold before receiving the next message

   * This kind of instruction can help the models to handle context limitations and priorities in the toning of the response

   * Again, this is another technique that relies on the fine-tuning of the model for instructions

2. Pass the initial prompt

   * Examples:

     ```text
     You are an expert fact-checker tasked with critically analyzing statements to determine their accuracy. For the given statement, please do the following:

     Assess the key claims being made in the statement. Break down the statement into its component assertions.

     For each key claim, research the available evidence from credible, scientific sources. Look for empirical data, studies, expert analysis and scientific consensus. Cite your sources.

     Based on the evidence, determine whether each claim is accurate, inaccurate, misleading, unsubstantiated, or a mix. Explain your reasoning, referring to the evidence.

     Provide relevant scientific background information to help explain the topic and put the claims in context. What is the nature of the phenomenon being discussed? What does scientific research say about it?

     Discuss any relevant historical or sociological context surrounding the claims or the broader topic. Have similar claims circulated before? Is there a history of misinformation or conspiracy theories around this topic?

     Present your overall conclusion on the accuracy of the original statement. Summarize the key evidence for and against it. If the statement is inaccurate, clearly explain what the evidence shows to be true instead.

     Use clear, precise language. Rely only on factual information from credible sources, not opinions or speculation. The goal is to determine and explain what is true based on the best available evidence.

     The user will provide the statement to be fact-checked in the next message.

     Answer this message with "OK" only.
     ```

     ```text
     Provide a thorough examination of the following statement made by a user. Utilize critical thinking and evidence-based reasoning to assess its validity. Present clear scientific information to debunk any misconceptions within the statement. Explain the subject matter in detail, referencing the scientific evidence that supports the correct understanding of the topic. Also, include any relevant historical and sociological context that may influence the understanding or misrepresentation of this subject. Ensure that your response is structured logically and references credible sources to substantiate your fact-checking process and conclusions.

     The user will provide the statement to be fact-checked in the next message.

     Answer this message with "OK" only.
     ```

3. Check if the model responded correctly with just `"OK"`

4. Pass the statement to be fact-checked

   * Considerations:

     * Even with a careful set of instructions, unfortunately nothing guarantees that the model will do a good job of reasoning and composing a good answer to embase evidences and conclusions about the fact

     * Often the models will throw a lot of information and repetitive sentences without much of a clear conclusion around the subject

     * Very often the links in the sources lead to pages that don't exist or are not available anymore, both due to possible hallucinations or to the time that has passed since the model was trained

       * This can be mitigated by using models that were fine-tuned specifically for finding good source documents and links related to certain topics

       * Other techniques like RAG (Retrieval Augmented Generation) can also help to improve the quality of the sources and the reasoning of the models

5. Evaluate the quality of the output

   * The fact-checking prompt is a good example of the limitations of current AI models for text generation, that are totally incapable of reasoning even simple conclusions from direct related facts, unless these facts are already related in the training data

6. Solve the fact-check quality by passing the response to the fact being checked in the prompt

   * Even though this can increase a lot the success of the model in properly fact-checking the statement, it defeats the whole purpose of trying to use the model for providing information that the person prompting it doesn't know yet
