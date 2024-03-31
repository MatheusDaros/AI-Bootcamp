# Using Vercel AI Playground

1. Create an account with [Vercel](https://vercel.com/)

2. Navigate to the [Vercel AI Playground](https://sdk.vercel.ai/)

3. Use the interface to compare different text generation models

   * Select two or three models to compare side by side

4. Compare using chat

   * Enable `Sync Chat` for a better comparison

5. Compare using prompts

   * Use the test prompt: `Sally (a girl) has 3 brothers. Each brother has 2 sisters. How many sisters does Sally have?`

   * Answer from `claude-3-opus`:

   ```text
   Okay, let's organize the information we have:

   Sally is a girl.
   Sally has 3 brothers.
   Each of Sally's brothers has 2 sisters.
   Now, let's think about this step by step:
   
   We know that Sally is a girl, so she is one of the sisters that each of her brothers has.
   
   Since Sally has 3 brothers, and each of these brothers has 2 sisters, you might think that there are 3 × 2 = 6 sisters in total. However, this is not correct.
   
   Remember, Sally is counted as a sister for each of her brothers. So, the other sister (who is not Sally) is counted 3 times, once for each brother.
   
   Therefore, there is only one other sister in the family besides Sally.
   
   So, the answer is that Sally has 1 sister.
   ```

   * Answer from `gpt-4-1106-preview`:

   ```text
   Sally has 3 brothers. Each brother has 2 sisters, but since we know Sally is one of the sisters, the other sister must be the same for all brothers. Therefore, Sally has only one sister, and together, they are the two sisters that each of the brothers has.
   ```

   * Answer from `mistral-large` (wrong):

   ```text
   Here's the logic behind this:

   We know that Sally is a girl and she has 3 brothers.
   Then we are told that each of her brothers has 2 sisters.
   Since Sally is one of the sisters to her brothers, there must be one more sister besides Sally for each brother to have 2 sisters.
   Therefore, Sally has 2 sisters in total - herself and the other sister mentioned in the question.
   ```

6. Compare more basic models using common riddles

   * Use the test prompt: `If you break me, I’ll not stop working. If you can touch me, my work is done. If you lose me, you must find me with a ring soon after. What am I?`

   * Answer from `gpt-3.5-turbo`:

   ```text
   The answer is a heart.
   ```

   * Answer from `llama-v2-70b-chat` (wrong):

   ```text
   You are a promise.

   A promise is a commitment or agreement to do something, and it continues to be in effect even if it is broken or damaged. If a promise is broken, it can be repaired or restored, and it continues to hold value as long as there is a willingness to make amends and keep the commitment.

   In the riddle, the phrase "if you break me" refers to the idea that a promise can be broken or damaged, but it can still be repaired or restored. The phrase "if you can touch me" suggests that a promise is intangible and cannot be physically touched, but it can still have a significant impact on relationships and outcomes. The final phrase "if you lose me" suggests that losing a promise can have negative consequences, but finding it again (with a ring) can help to restore trust and repair relationships.

   Overall, the riddle highlights the importance of keeping promises and maintaining trust in relationships. It emphasizes the idea that promises are not easily broken or discarded, and that they continue to hold value even when they are broken or damaged.
   ```

   * Answer from `mistral-8x7b` (wrong):

   ```text
   The answer is a fuse. The reasoning behind this is that when a fuse breaks or blows, it still allows electricity to flow until it is replaced; you can touch it while it's working but once it does its job (protecting the circuit), it becomes useless; and if you lose a fuse by it blowing, you need to find a replacement quickly to restore function.
   ```

7. Compare different models using basic math

   * Use the test prompt: `What is the modulus of 20 by 3?`

   * Answer from `gpt-3.5-turbo`:

   ```text
   The modulus of 20 divided by 3 is 2.
   ```

   * Answer from `llama-v2-70b-chat` (wrong):

   ```text
   Sure, I'd be happy to help! The modulus of 20 by 3 is 6.
   ```

   * Answer from `mistral-8x7b`:

   ```text
   The modulus or remainder of dividing 20 by 3 is 2. This is because when 20 is divided by 3, the quotient is 6 with a remainder of 2. You can also find the remainder by subtracting the largest multiple of 3 less than 20 (which is 18) from 20, so 20 - 18 = 2.
   ```

   * Answer from `claude-3-opus`:

   ```text
   The modulus operation (also known as the remainder operation) returns the remainder after dividing one number by another. It is denoted by the "%" symbol.

   To find the modulus of 20 by 3, we divide 20 by 3 and keep the remainder.

   20 ÷ 3 = 6 remainder 2

   Therefore, the modulus of 20 by 3 is 2.

   In other words, 20 % 3 = 2.
   ```

   * Answer from `gpt-4-1106-preview`:

   ```text
   The modulus (often referred to as the remainder) of 20 by 3 is the remainder when you divide 20 by 3.

   To calculate this, you divide 20 by 3, which equals 6 with a remainder of 2, since 3 times 6 equals 18, and you have 2 left over to reach 20.

   So the modulus of 20 by 3 is 2.
   ```

   * Answer from `mistral-large`:

   ```text
   The modulus operation, often denoted by the percent sign % in many programming languages, is used to find the remainder of a division operation. In this case, you're asking for the modulus of 20 by 3, which is equivalent to asking "what is the remainder when 20 is divided by 3?"

   When you divide 20 by 3, you get 6 with a remainder of 2. Therefore, the modulus of 20 by 3 is 2.
   ```
