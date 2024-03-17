# Using Text Generation WebUI to Process Instructions

1. Load a model fine-tuned for instruction-following tasks

2. Select `Chat` tab

3. Click in the `Show controls` checkbox

4. Scroll down to see the control options

5. Change the mode to `Instruct`

   * It is still possible to send chat messages to the model in this mode, but the prompt structure is not ideal for this kind of conversation and the results can be very erratic

6. Type an instruction in the chat interface and hit `Generate`

   * For example, ask the model to `Write a short story about Pirates`

   * You can give sequential instructions in the same prompt, like `Start the story with a shipwreck`, `Include a treasure map`, `Include a Pirate named Jake` and `Make the story finish with a funny twist`

   * Example of answer:

     ```text
     Once upon a time, in the vast and untamed ocean, there was a group of pirates led by Captain Jack Sparrow himself. They had set sail on their quest for hidden treasures, unaware of the storm brewing ahead. The skies darkened, and the waves grew bigger by the minute. Soon enough, their ship was hit by a violent wave, sending them all flying across the deck. As they struggled to regain control, another huge wave crashed into the ship, tearing it apart piece by piece. The crew members scattered everywhere, clinging onto anything that could save them from drowning.

     Jake, a young buccaneer who had just joined the crew, found himself floating amidst the wreckage. He managed to grab hold of a piece of wood that served as his only lifeline. As he looked around, hoping to spot any other survivors, something caught his eye - a small parchment scroll floating nearby. With shaky hands, he reached out and retrieved it from the water. Unrolling the scroll carefully, he gasped in surprise; it was a treasure map!

     The map showed an X marking a location deep within an island far away from where they were stranded. Determined to follow the map's lead, Jake began swimming towards the distant shore. Hours passed, and his arms felt like jelly from exhaustion. But finally, he reached the shore, collapsing onto the sandy beach. As he rested, trying to catch his breath, he noticed a group of local villagers gathered around him, staring at him curiously. One of them approached cautiously, holding out a coconut filled with fresh water.

     "Thank ye kindly," said Jake weakly, taking the drink gratefully. "I was wondering if ye happened to see any buried treasure 'round these parts?"

     The villagers exchanged puzzled glances before bursting into laughter. One of them pointed behind Jake, revealing two crossed lines of palm trees swaying gently in the breeze.

     "That be our village idiot," they chuckled
     ```

7. If you feel that the GPT has not finished the set of instructions yet, you can click on `Continue` to make the model generate more text based on the same last prompt

   * You might need to increase the `max_new_tokens` parameter in the `Parameters` tab to allow the model to generate more text to fulfill the given instructions
