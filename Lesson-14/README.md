# Lesson 14: AI Image Generation

TODO

## Pre-requisites

## Review of Lesson 13

TODO

## Prompting Techniques for Image Generation

* Overall considerations
  * Best techniques for each kind of models
  * Positive prompts
  * Negative prompts
  * Embeddings present or not in the training data
* Positive prompts guidelines
  * Structure: Specify as clearly as possible what are the major defining elements in the image
    * Subject: "Generate an image of {object}" where {object} is the name of the object/element you want to generate
      * Be as specific as possible, and consider if this word is well represented in the training data
      * Sometimes it's better to use a more general terms than specific ones
      * If desired, add an action: "Generate an image of {object} {action}", for example "standing", "running", "flying", etc.
    * Specify form, quantity and adjectives: "Generate an image of {quantity} {quality} {adjective} {object}"
      * Not all models are trained to handle these kind of prompts
        * Prompts like "two big sweet red apples" might not behave the way you expect in many models
  * Context: Specify the image composition elements, like settings, style and artistic form
    * Specify if it is a portrait, a landscape, a still life, etc.
    * Specify if it should look like a photography, a painting, a drawing, sculpture, etc.
    * Define the details of the composition, like the background, the lighting, the colors, etc.
      * Add specifications like "close-up", "far away", "profile", etc.
    * Depending on the model training, you can specify the style of the image, like "impressionist", "surreal", "realistic", etc.
      * If a model is trained with a specific artist's work, you can even specify the artist's name
      * But if the model training data has no mentions to it, the results could be totally different from what you expect
  * Refinements: Some models can handle more specific instructions to refine and add nuances to the image
    * Specify the mood of the image, like "happy", "sad", "scary", etc.
    * Specify the time of the day, the weather, the season, etc.
    * Control the lighting, color scheme or temperature, detail level, realism level, and such
  * Tip: to test if a model understand a term, try generating an image of it without any other prompt, just the word you want to test
    * For example, before generating "A happy futuristic landscape picture of Darth Vader riding a blue unicorn", try generating just "Darth Vader" and also "Unicorn" separately, and see if they are well represented in the outputs
* Negative prompts
  * Some models accept negative prompts to instruct certain elements or aspects to be avoided in the generated image
  * Applying negative prompts may reduce the probabilities of certain flaws or deformations in the generated images, but also they can limit the quality of the generated images
  * Different subjects may require different sets of negative prompts to work properly
    * For example, for living creatures you can include negative prompts like: deformed, ugly, too many fingers, too many limbs
      * For objects, you can include more generalist terms like: duplicated, blurry, pixelated, low quality, out of frame, cropped
      * For faces, depending in the pose and the close-up, you can include negative prompts like: poorly rendered face, deformed, disfigured, long neck, ugly
      * For landscapes, you can include negative prompts like: blurry, pixelated, out of frame, cropped, text, watermark, low quality, poorly drawn, pixelated
* Prompt examples
  * [Prompt Templates](https://github.com/Dalabad/stable-diffusion-prompt-templates) repository
  * [Prompt Presets](https://openart.ai/presets) from OpenArt
* The [StyleSelectorXL](https://github.com/ahgsql/StyleSelectorXL) extension

## Useful Configurations for Stable Diffusion WebUI

* Using the [Local API](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/API)
* Installing and managing extensions
* Application configurations
  * Running in [Low VRAM](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Troubleshooting#low-vram-video-cards)
  * Running in [CPU mode](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#running-on-cpu)

## Generating Images with Python

* Practical exercises
  * Exercise 1: [Photorealistic image generation](./project/00-Generate-Photo.md) by running a script with a preconfigured prompt
    * Code [GeneratePhoto.py](./project/GeneratePhoto.py) and run it by passing a name of an object as argument
  * Exercise 2: [Cartoon sequence generation](./project/01-Generate-Cartoon.md)
    * Code [GenerateCartoon.py](./project/GenerateCartoon.py) and run it to generate four images of a cartoonish bomb explosion in a sequence

## Using a ControlNet

* The problem of controlling the diffusion process
* Using a ControlNet to guide the diffusion process
  * Image consistency
  * Poses and positions
  * Style transfer
  * Colorization
  * Shapes, edges and outlines
  * Depth maps
  * Semantic segmentation
  * Shuffles
  * Image manipulation with instructions
  * Inpaint masks
  * Tiles
* Installing and using the [ControlNet](https://github.com/Mikubill/sd-webui-controlnet) extension
  * Downloading a [Compatible Model](https://github.com/Mikubill/sd-webui-controlnet?tab=readme-ov-file#download-models)
* Parameters
  * Input image
  * Enable
  * Low VRAM
  * Control Type
  * Preprocessor
  * Model
  * Control Weight
  * Starting Control Step
  * Ending Control Step
  * Control Mode
  * Resize Mode

## Generating Images with a ControlNet

* Practical exercises
  * Exercise 3: Experiment with [Consistent Portrait Generation](./project/02-Generate-Portrait.md) using the ControlNet to generate eight portrait pictures of the same fictional character
  * Exercise 4: Generate a [QR Code Art](./project/03-Generate-QRCode.md) to a website using the ControlNet

## Next steps

TODO
