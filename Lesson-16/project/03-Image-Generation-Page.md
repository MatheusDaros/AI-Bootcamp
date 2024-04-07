# Implementing Image Generation in an Application

1. Create a page to generate images with an image generation model

2. The user may click on "Generate Image" to create a new image based in the last message of the story generated in the chat

3. When clicking the button, the page should first ask the text generation model to generate a new message detailing exactly what is happening at the scene of the story at that moment

4. After the message is generated, it must not be displayed in the chat, but instead it should be used as the prompt for the image generation model

5. When the image is generated, it should be displayed on the page bellow the last message of the chat
