# Generating an image with a specify human pose using ControlNet

1. Download a model to use as `Stable Diffusion checkpoint`

   * Download `Ghostmix` model [here](https://civitai.com/api/download/models/76907?type=Model&format=SafeTensor&size=pruned&fp=fp16)
  
   * Place the downloaded file in the `stable-diffusion-webui/models/Stable-diffusion` directory

2. Download a model to use with `ControlNet openpose` preprocessor

   * Download `control_v11p_sd15_openpose.pth` model [here](https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth?download=true)
  
   * Place the downloaded file in the `stable-diffusion-webui/extensions/sd-webui-controlnet/models` directory

3. Select the model to use as the `Stable Diffusion checkpoint`

   * Click on the refresh icon and select `Ghostmix`. This will set the model that we downloaded in step 1 as the `Stable Diffusion checkpoint`

   * Use `a young male, outside a restaurant, brown eyes` as the prompt and `ugly, disfigured, low quality, nsfw, bad, immature` as the negative prompt

   ![txt2img settings](../project/images/image6.png)

4. Use the following settings in the `Generation` tab:

   * Sampling Method: `DPM++ 2M Karras`

   * Sampling Steps: `25`

   * Width: `512`

   * Height: `512`

   * CFG Scale: `7`

   * ![generation settings](../project/images/image7.png)

5. Configure ControlNet

   * On the text2img page, expand the ControlNet section. You should see an empty image canvas under ControlNet Unit 0 > Single Image.

   * Upload the `pose.jpg` file located inside the `images` folder of this directory

     ![pose](../project/images/pose.jpg)
  
   * Mark the `Enable` checkbox

   * Use the following settings:

      * Preprocessor: `Dw_openpose_full`

      * ControlNet Model: `Control_v11p_sd15_openpose [cab727d4]`

      ![controlnet](../project/images/image8.png)

6. Press the `Generate` button to view the result

   * The preprocessor should be able to extract the pose from the uploaded image and generate a "skeleton" that will be used to generate the final image

     ![pose skeleton](./images/pose-skeleton.png)

   * The ControlNet model will then use the pose information to generate an image conforming to these instructions

     ![example](./images/example2.png)

7. Copy the `Seed` value from the generated image and paste it in the `Seed` field in the `Generation` tab

   ![generation seed](./images/generation-seed.png)

   * The output image should always look similar in subsequent generations when locking the seed

8. Modify the pose with the `OpenPose Editor`

   * You can remove the initial image since the pose is already extracted

   * Select the `Edit` button to open the `OpenPose Editor`

   ![open pose editor](./images/open-pose.png)

9. Edit the pose until you have the desired result

   ![edited pose](./images/pose-edit.png)

   * You may drag each node to adjust the pose as desired

   * You can select groups of nodes to move, rotate and resize them together, useful for complex features like faces and hands

   * Once you are satisfied with the pose, press the `Send pose to ControlNet` button to save the changes

10. Press the `Generate` button to generate another image

    ![pose result](./images/pose-result.png)

    * By locking the seed value, the generated person should look very alike to the previous one, but with the new pose

    * This way you can generate different images of the same fictional character in different poses without having to manually edit one by one in a graphic editor

    * You can repeat the process with little incremental changes to create frames of a video animation
