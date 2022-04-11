# E7 Secret Shop Auto Refresh Macro
This macro helps the user refresh the Secret Shop and buy Covenant and Mystic bookmarks. The mouse clicks and delay intervals are randomized to avoid Epic Seven detecting the use of third-party software. 

This code is heavily referenced from Epic_Scripted's [E7-Auto-Shop-Refresh-Custom](https://github.com/EpicScipted/E7-Auto-Shop-Refresh-Custom), as well as the [original script](https://github.com/EmaOlay/E7-Auto-Shop-Refresh) is made by EmaOlay.

[![Watch the video](https://i.imgur.com/guAqhAF.png)](https://i.imgur.com/XU3MSgI.mp4)

## How to Run:
1. Make sure you have Python and the correct dependencies installed (see below)
2. Set your resolution to 1920x1080. This macro will not work for other resolutions
3. Open and maximize Bluestacks
4. Open Epic Seven, then enter Secret Shop
	Make sure you have enough gold and skystones!
	Macro should exit automatically if you run out, but this has NOT BEEN TESTED
5. Run the Python script
	If running from terminal, make sure the refresh button is visible on the screen
6. If running the script for the first time, make sure everything works correctly first
	If the macro is not recognizing the images properly, you will need to replace the images in the folder with your own screenshots
7. To exit the script, hold 'q' until the macro stops working completely

## Dependencies to Install
Use the package manager [pip](https://pip.pypa.io/en/stable/installation/) to install the following dependencies:
```
pip install keyboard
pip install opencv-python
pip install pyautogui
pip install mouse
```
