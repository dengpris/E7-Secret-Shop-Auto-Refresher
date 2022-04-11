"""
Created on Sun Apr 10 2022

@author: Zalkyrie
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#BEFORE USING THE MACRO it is recommended to first test the program
#If there are bookmarks in shop and the program does not detect it --
#you may need to replace the images with your own

#TO EXIT THE MACRO, hold 'q' until the program stops

#Code currently requires maximized Bluestacks window, 1080p
#If starting the macro from terminal, MAKE SURE REFRESH BUTTON IS VISIBLE

#If you run out of gold or skystones, macro should exit

# use for debugging, this sets delay between clicking refresh and confirm
# 0 default, set to 1-2 seconds when testing (so you can click q to exit if script goes wrong)
debug_timer = 0.5

#Specify how long this program should be run for
run_timeout = int(input("How long should this macro be run for? (Enter in minutes): "))*60
start_time = time.time()

timeout = 5 #if program hangs for 5 seconds, terminate
time.sleep(2) #wait 2 seconds in case user needs to click into bluestacks

#Locate refresh button
RB_pos=pyautogui.locateOnScreen('refresh_button.png',confidence=0.8)
#If refresh button is not found, you may need to replace the images with your own
if (RB_pos == None):
    print("Error: Refresh button not found.")
    quit

while ((keyboard.is_pressed('q') == False) and (time.time() < start_time+run_timeout)):
    #The confidence is added due to little variations in the background
    Coven_pos=pyautogui.locateOnScreen('covenant.png',confidence=0.8)
    Mystic_pos=pyautogui.locateOnScreen('mystic.png',confidence=0.8)   

    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
#Checks for covenant
    if (Coven_pos) != None:       
        print("Buy Covenant Summons.")
        
        #Locate buy button
        Coven_point=pyautogui.center(Coven_pos)
        click(Coven_point[0]+800+rand_x, Coven_point[1]+40+rand_y)
        click(Coven_point[0]+800+rand_x, Coven_point[1]+40+rand_y)
        time.sleep(random.uniform(0.2, 0.4)) #wait for confirm button
        
	#Confirm buy
        timeout_start = time.time() 
        while(time.time() < (timeout_start + timeout)):
            Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.png', confidence=0.8)
            if (Buy_button_Covenant_pos != None):
                break

        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0]+rand_x, Buy_button_Covenant_point[1]+rand_y)
        click(Buy_button_Covenant_point[0]+rand_x, Buy_button_Covenant_point[1]+rand_y)

    else:
        print("No Covenant summons to buy.")       

#checks for mystic
    if (Mystic_pos != None):
        time.sleep(random.uniform(0.2, 0.4))      
        print("Buy Mystic Summons.")
	
        #Locate buy button
        Mystic_point=pyautogui.center(Mystic_pos)
        click(Mystic_point[0]+800, Mystic_point[1]+40)
        click(Mystic_point[0]+800, Mystic_point[1]+40)
        time.sleep(random.uniform(0.2, 0.5)) #wait for confirm button
        
	#Confirm buy
        timeout_start = time.time()
        while(time.time() < (timeout_start + timeout)):
            Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.png', confidence=0.8)
            if (Buy_button_Mystic_pos != None):
                break

        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0]+rand_x, Buy_button_Mystic_point[1]+rand_y)
        click(Buy_button_Mystic_point[0]+rand_x, Buy_button_Mystic_point[1]+rand_y)
        
    else:
        print("No Mystic summons to buy.")

    time.sleep(random.uniform(0.2, 0.3))
    scroll_pt_x = random.randint(1100,1550)
    scroll_pt_y = random.randint(400,680)

    click(scroll_pt_x, scroll_pt_y)
    pyautogui.scroll(-random.randint(3,7), x=scroll_pt_x, y=scroll_pt_y)

    time.sleep(0.5)
    Coven_pos2=pyautogui.locateOnScreen('covenant.png',confidence=0.8)
    Mystic_pos2=pyautogui.locateOnScreen('mystic.png',confidence=0.8)
	
#Checks for covenant
    if ((Coven_pos2 != None) and (Coven_pos == None)):
        time.sleep(0.2)
        print("Buy Covenant Summons.")

        #Locate buy button
        Coven_point=pyautogui.center(Coven_pos2)
        click(Coven_point[0]+800, Coven_point[1]+40)
        time.sleep(random.uniform(0.2, 0.4)) #wait for confirm button

        #Confirm buy
        timeout_start = time.time() 
        while(time.time() < (timeout_start + timeout)):
            Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.png', confidence=0.8)
            if (Buy_button_Covenant_pos != None):
                break

        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        click(Buy_button_Covenant_point[0]+rand_x, Buy_button_Covenant_point[1]+rand_y)
        click(Buy_button_Covenant_point[0]+rand_x, Buy_button_Covenant_point[1]+rand_y)
	
    else:
        print("No Covenant summons to buy.")
        
#checks for mystic
    if ((Mystic_pos2 != None) and (Mystic_pos == None)):
        time.sleep(0.2)        
        print("Buy Mystic Summons.")
        
        #Locate buy button
        Mystic_point=pyautogui.center(Mystic_pos2)
        click(Mystic_point[0]+800, Mystic_point[1]+40)
        time.sleep(random.uniform(0.2, 0.3)) #wait for confirm button

        #Confirm Buy
        timeout_start = time.time()
        while(time.time() < (timeout_start + timeout)):
            Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.png', confidence=0.8)
            if (Buy_button_Mystic_pos != None):
                break

        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        click(Buy_button_Mystic_point[0]+rand_x, Buy_button_Mystic_point[1]+rand_y)
        click(Buy_button_Mystic_point[0]+rand_x, Buy_button_Mystic_point[1]+rand_y)
	
    else:
        print("No Mystic summons to buy.")
        
#Finally refreshes
    #time.sleep(random.uniform(0.2, 0.3))
#When testing, pause to allow user to exit
    debug_time_start = time.time()
    while (time.time() < debug_time_start+debug_timer):
        if (keyboard.is_pressed('q') == True):
            quit
    
    RB_point=pyautogui.center(RB_pos)
    click(RB_point[0]+rand_x, RB_point[1]+rand_y)
    click(RB_point[0]+rand_x, RB_point[1]+rand_y)
    time.sleep(0.1) #wait for confirm to appear
    
    timeout_start = time.time()
    while(time.time() < (timeout_start + timeout)):
        Confirm_pos=pyautogui.locateOnScreen('confirm_button.png', confidence=0.5)
        if (Confirm_pos != None):
            break

#Confirm refresh
    Confirm_point=pyautogui.center(Confirm_pos)
    click(Confirm_point[0]+rand_x, Confirm_point[1]+rand_y)
    click(Confirm_point[0]+rand_x, Confirm_point[1]+rand_y)
    time.sleep(0.5)
        
