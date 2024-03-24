# Text Generation WebUI Installation Steps

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/oobabooga/text-generation-webui.git
   ```

2. Change to the `text-generation-webui` directory:

   ```bash
   cd text-generation-webui
   ```

3. Run the installation script:

   * Use `start_linux.sh` script for Linux

   ```bash
   ./start_linux.sh
   ```

    * Use `start_windows.bat` script for Windows in cmd

    ```bash
    start_windows.bat
    ```

    * Use `start_macos.sh` script for MacOS

    ```bash
    ./start_macos.sh
    ```

    * Use `start_wsl.bat` script for Windows Subsystem for Linux

    ```bash
    start_wsl.bat
    ```

4. Wait for the download and installation of dependencies to finish

5. When prompted, select your GPU manufacturer and model

   * You will see a list of available GPUs, select the one that matches your system by typing the corresponding letter and pressing `Enter`

   ```bash
   What is your GPU?
   A) NVIDIA
   B) AMD (Linux/MacOS only. Requires ROCm SDK 5.6 on Linux)
   C) Apple M Series
   D) Intel Arc (IPEX)
   N) None (I want to run models in CPU mode)
   ```

   * If you don't have a GPU, select `N` to run the models in CPU mode

6. Confirm selection and wait until the entire installation process finishes

   * The installation process may take a while depending on your internet connection and system specifications

     * The script should start downloading all packages in sequence

     * After all downloads are complete, the script will start installing the packages and configuring everything automatically

       * If you get any errors during the installation process, please check the error message and look for any possible missing dependencies or prerequisites

   * Look for a message saying `Successfully installed ...` at the end of the installation process

   * If is the first time installing this repository, you should also see this message:

   ```text
   *******************************************************************
   * You haven't downloaded any model yet.
   * Once the web UI launches, head over to the "Model" tab and download one.
   *******************************************************************
   ```

   * The last message in your terminal should be:

   ```text
   Running on local URL:  http://127.0.0.1:7860
   ```

   * The process is going to keep continuously running after this message

     * If you close this terminal window, the process will stop running

     * If you want to stop the application, you can press `Ctrl + C` (or `Cmd + C` for MacOS) in the terminal

7. Open your browser and go to <http://localhost:7860> to test if the application is working

8. You can use this same script to start the application in the future

   * The script will automatically detect that everything is already installed and will just start the application
