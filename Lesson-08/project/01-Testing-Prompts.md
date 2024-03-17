# Testing prompts formats and techniques

1. Use the `chat` tab of the Text Generation WebUI to test different prompts for text generation tasks

2. Testing basic prompts for creative tasks

   ```text
   You are a scientist who has discovered a new planet capable of supporting human life. Write a report detailing your findings, including the planet's climate, geography, potential resources, and any unique features. Discuss the potential benefits and challenges of human colonization on this planet.
   ```

   ```text
   Imagine you are a time traveler who has been sent back to the medieval period. Write a journal entry detailing your experiences, including your interactions with the people, your observations about their way of life, and the challenges you face trying to fit in. Reflect on how this experience changes your perspective about the present.
   ```

   ```text
   Write a haiku about the beauty of a sunset, incorporating vivid sensory details.
   ```

3. Testing short prompts for specific tasks

   ```text
   Explain the concept of photosynthesis in simple terms suitable for a 5th-grade science class.
   ```

   ```text
   Generate a creative and attention-grabbing headline for an article about the benefits of meditation.
   ```

   ```text
   Summarize the main benefits of renewable energy in one sentence.
   ```

   ```text
   List three unique adaptations of the Arctic fox that allow it to thrive in polar environments.
   ```

4. Testing chain of thought prompting examples

   * This kind of prompt works very well with models fine-tuned for instructions

   ```text
   Explain how a bill becomes a law in the United States. Begin by describing the initial drafting process, followed by the steps of committee review, debates, voting procedures in both the House of Representatives and the Senate, the role of conference committees in reconciling different versions of the bill, and finally, the President's options upon receiving the passed bill.
   ```

   ```text
   Describe the process of making a cup of coffee, from selecting the beans to brewing the coffee. Include the steps of grinding the beans, preparing the filter, boiling the water, pouring the water over the coffee grounds, and waiting for the coffee to brew.
   ```

   ```text
   Explain the process of photosynthesis in plants, from the absorption of sunlight to the production of glucose. Include the steps of capturing light energy, converting it into chemical energy, and using it to synthesize organic compounds.
   ```

5. Testing prompts for creative storytelling with constraints:

   * This is another example of prompt technique that benefits from instruction fine-tuned models

   ```text
   Compose a short story set in a dystopian future where artificial intelligence governs humanity. Introduce a protagonist who is a part of the resistance movement. The story should weave themes of hope, individual freedom, and the importance of human connection. Include a pivotal scene where the protagonist discovers a hidden truth about the AI overlords that changes the course of the rebellion. Conclude with an open-ended finale that invites the reader to ponder the balance between technology and human agency.
   ```

   ```text
   Write a story about a character who discovers a magical telephone booth that grants them the ability to time travel. The story should explore the character's moral dilemmas and the consequences of their actions as they navigate through different time periods. Include a plot twist that challenges the character's understanding of cause and effect, and conclude with a reflection on the nature of fate and free will.
   ```

   ```text
   Create a narrative about a group of astronauts who embark on a perilous mission to explore a distant exoplanet. The story should mention the hitchhiker's guide to the galaxy. The narrative should include moments of tension, wonder, and discovery, and it should culminate in a surprising twist that redefines the astronauts' understanding of the universe.
   ```

6. Testing prompts for assisting in real world situations

   * This is the most challenging kind of prompt to adjust, since small nuances or peculiarities of these situations could alter a lot the desired results of the prompt

   * Unfortunately there is no one-size-fits-all solution for real world situations, like marketing, sales, engineering or scientific tasks

   * The more specific you write the prompt, the more likely you are to get the desired results from very similar situations

   * Examples:

     ```text
     You are a travel writer tasked with creating a compelling blog post about a hidden gem destination. Choose a lesser-known location and write a 500-word article that highlights its unique features, culture, and attractions. Use descriptive language and storytelling techniques to engage the reader and make them want to visit the destination. Include practical information such as how to get there, the best time to visit, and must-see attractions.
     ```

     ```text
     As an expert in personal finance, you have been asked to write a comprehensive guide on creating and sticking to a budget. In 800 words, cover the following points: a) The importance of budgeting and its benefits b) How to assess one's current financial situation and set realistic goals c) Steps to create a budget, including identifying income, categorizing expenses, and allocating funds d) Tips for tracking expenses and staying accountable e) Strategies for cutting costs and finding additional sources of income f) How to adjust a budget when faced with unexpected expenses or life changes Use clear, concise language and provide practical examples to make the guide accessible and actionable for readers at various stages of their financial journey.
     ```

     ```text
     You are a marketing consultant tasked with creating a social media campaign for a new line of eco-friendly household products. Develop a series of engaging social media posts that highlight the products' sustainability, affordability, and effectiveness. Use persuasive language and visual storytelling to capture the attention of environmentally conscious consumers and encourage them to consider the products for their homes. Include a mix of informative, entertaining, and interactive content to drive engagement and brand awareness. All the communications should either entertain, educate or inspire the audience. Work in the delivery of the message in a way that it is not intrusive or annoying, but rather engaging and compelling.
     ```

     ```text
     You are a software engineer tasked with writing a technical documentation for a new software library. The documentation should cover the following aspects: a) An overview of the library's purpose and key features b) Installation and setup instructions c) A detailed explanation of the library's API, including input parameters, return values, and usage examples d) Best practices and coding conventions for using the library e) Troubleshooting tips and common error messages f) A roadmap for future updates and contributions. Use clear, concise language and provide code snippets and diagrams to enhance the readability and usability of the documentation.
     ```

     ```text
     You are a software teacher preparing a hands-on bootcamp about the applications of AI. Write a lesson plan for a 3-hour workshop that introduces students to the basics of AI, machine learning, and natural language processing. The lesson plan should include: a) An overview of the workshop's objectives and target audience b) A detailed schedule with time allocations for each topic and activity c) A list of required materials and resources, including software, datasets, and reference materials d) A series of interactive exercises and demonstrations to engage students and reinforce key concepts e) Assessment methods and feedback mechanisms to evaluate students' understanding and progress. Use a mix of lecture-style presentations, group discussions, and hands-on coding exercises to create an engaging and effective learning experience. Include casual jokes and food references to keep the students engaged and entertained.
     ```