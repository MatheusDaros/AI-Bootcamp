# Using OpenAI Chat Playground

1. Go to [Open AI Chat Playground](https://platform.openai.com/playground?mode=chat)
2. Use the following parameters:
   * System settings:

     “_You are a knowledgeable and resourceful virtual travel advisor, expertly equipped to assist with all aspects of travel planning. From suggesting hidden gems and local cuisines to crafting personalized itineraries, you provide insightful, tailored travel advice. You adeptly navigate through various travel scenarios, offering creative solutions and ensuring a delightful planning experience for every traveler._”

   * User prompt:

     “_Hello! I'm dreaming of an adventure and need your help. I want to explore a place with breathtaking landscapes, unique culture, and delicious food. Surprise me with a destination I might not have thought of, and let's start planning an unforgettable trip!_”

   * Configurations:
     * Model: `gpt-3.5-turbo`
     * Temperature: `0.75`
     * Max tokens: `500`
     * Top p: `0.9`
     * Frequency penalty: `0.5`
     * Presence penalty: `0.6`
3. Click on `Submit`
4. Wait for the response for `Assistant`
5. Add another user message: "_What to avoid there?_"
6. Click on `Submit`
7. Wait for the response for `Assistant`
8. Keep experimenting with other messages and parameters

## Parameters

* Agent description: This plays a crucial role in guiding the AI's behavior and response style. Different descriptions can set the tone, personality, and approach of the model. 
For instance, using a description such as "You are a creative storyteller" would prompt the AI to adopt a more imaginative and narrative style, whereas "You are a technical expert" might lead to more detailed and specific technical information in responses.

* Temperature: This controls the randomness of the responses.
A lower temperature (e.g., 0.0-0.3) results in more predictable, conservative responses, ideal for factual or specific queries. A higher temperature (e.g., 0.7-1.0) generates more creative and varied responses, useful for brainstorming or creative writing.

* Max Tokens (Length): This sets the maximum length of the response.
For concise, straightforward answers, a lower range (e.g., 50-100 tokens) is suitable. For more detailed explanations or narratives, a higher range (e.g., 150-500 tokens) can be used.

* Frequency Penalty: This reduces the likelihood of the model repeating the same word or phrase. A lower setting (e.g., 0.0-0.5) allows some repetition, which can be useful for emphasis in writing or speech. A higher setting (e.g., 0.5-1.0) minimizes repetition, helpful for generating diverse and expansive content.

* Presence Penalty: This discourages the model from mentioning the same topic or concept repeatedly. A lower setting (e.g., 0.0-0.5) is suitable for focused content on a specific topic, while a higher setting (e.g., 0.5-1.0) encourages the model to explore a wider range of topics, useful for brainstorming or exploring different aspects of a subject.

* Top P (Nucleus Sampling): This determines the breadth of word choices considered by the model. A lower setting (e.g., 0.6-0.8) leads to more predictable text, good for formal or factual writing. A higher setting (e.g., 0.9-1.0) allows for more creativity and divergence, ideal for creative writing or generating unique ideas.

>You can learn more about these parameters at <https://platform.openai.com/docs/api-reference/chat/create>
