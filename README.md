# E7 Secret Shop Auto Refresh Macro
This macro helps the user refresh the Secret Shop and buy Covenant and Mystic bookmarks. The mouse clicks and delay intervals are randomized to avoid Epic Seven detecting the use of third-party software. 

This code is heavily referenced from Epic_Scripted's [E7-Auto-Shop-Refresh-Custom](https://github.com/EpicScipted/E7-Auto-Shop-Refresh-Custom), as well as the [original script](https://github.com/EmaOlay/E7-Auto-Shop-Refresh) is made by EmaOlay.

![](https://media.giphy.com/media/NSAX9N2SyPUVrih2E0/giphy-downsized-large.gif)

## How to Run:
1. Make sure you have [Python](https://www.python.org/downloads/) and the correct dependencies installed (see below)
2. Set your resolution to 1920x1080. This macro will not work for other resolutions
3. Open and maximize Bluestacks
4. Open Epic Seven, then enter Secret Shop
5. Run the Python script
	>If running from terminal, make sure the refresh button is visible on the screen
6. If running the script for the first time, make sure everything works correctly first
	>If the macro is not recognizing the images properly, you will need to replace the images in the folder with your own screenshots
7. To exit the script, hold 'q' until the macro stops working completely
    > Script will exit after confirming refresh. Set 'debug_timer' greater than 0 to exit before refresh.

## Dependencies to Install
Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) to install the following dependencies:
```
pip install keyboard
pip install opencv-python
pip install pyautogui
pip install mouse
```
