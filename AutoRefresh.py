"""
Created on Sun Apr 10 2022

@author: Zalkyrie
"""

from pyautogui import *
import pyautogui
import time
import datetime
import keyboard
import random
import win32api, win32con
import sys

############### HELPER FUNCTIONS ###############
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.4)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def buy(bookmark):
    bought = False
    pos = None
    buy_start = time.time() 

    while((pos == None) and (time.time()< (buy_start + timeout))):
        if (bookmark == 'covenant'):
            pos = pyautogui.locateOnScreen('covenant.png',confidence=0.8)
        else:
            pos = pyautogui.locateOnScreen('mystic.png',confidence=0.8)

    pos_point = pyautogui.center(pos)
    #click buy
    click(pos_point[0]+800+rand_x, pos_point[1]+40+rand_y)
    click(pos_point[0]+800+rand_x, pos_point[1]+40+rand_y)
    time.sleep(random.uniform(0.2, 0.4)) #wait for confirm button

    #Confirm buy
    timeout_start = time.time() 
    Buy_button_pos = None
    while(time.time() < (timeout_start + timeout)):
        if (bookmark == 'covenant'):
            Buy_button_pos=pyautogui.locateOnScreen('Buy_button_Covenant.png', confidence=0.6)
        else:
            Buy_button_pos=pyautogui.locateOnScreen('Buy_button_Mystic.png', confidence=0.6)

        if (Buy_button_pos != None):
            Buy_button_point=pyautogui.center(Buy_button_pos)
            click(Buy_button_point[0]+rand_x, Buy_button_point[1]+rand_y)
            click(Buy_button_point[0]+rand_x, Buy_button_point[1]+rand_y)

            bought = True
            break

    #if bought is not true here, something went wrong
    if (bought == False):
        global exit_flag
        exit_flag = 1
        
################# HELPERS END #################

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
exit_flag = 0
time.sleep(2) #wait 2 seconds in case user needs to click into bluestacks

#Specify how long this program should be run for
run_timeout = float(input("How long should this macro be run for? (Enter in minutes): "))*60
start_time = time.time()
start_datetime = datetime.datetime.now()

timeout = 5 #if program hangs for 5 seconds, terminate

#Locate refresh button
RB_pos=pyautogui.locateOnScreen('refresh_button.png',confidence=0.8)
#If refresh button is not found, you may need to replace the images with your own
if (RB_pos == None):
    print("Error: Refresh button not found.")
    quit

#Counter (will tell you how many mystics/covenants were bought at the end)
mystic_count = 0
covenant_count = 0
refresh_count = 0

while ((exit_flag == 0) and (time.time() < start_time+run_timeout)):
    #The confidence is added due to little variations in the background
    Coven_pos=pyautogui.locateOnScreen('covenant.png',confidence=0.8)
    Mystic_pos=pyautogui.locateOnScreen('mystic.png',confidence=0.8)   

    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
#Checks for covenant
    if (Coven_pos) != None:       
        buy('covenant')
        covenant_count=covenant_count+1  

#Checks for mystic
    if (Mystic_pos != None):
        time.sleep(random.uniform(0.2, 0.4))      
        buy('mystic')
        mystic_count=mystic_count+1

#Scroll down
    time.sleep(random.uniform(0.2, 0.4))
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
        buy('covenant')
        covenant_count=covenant_count+1
        
#checks for mystic
    if ((Mystic_pos2 != None) and (Mystic_pos == None)):
        time.sleep(0.2)        
        buy('mystic')
        mystic_count=mystic_count+1
        
#Finally refreshes
#When testing, pause to allow user to exit
    debug_time_start = time.time()
    while (time.time() < debug_time_start+debug_timer):
        if (keyboard.is_pressed('q') == True):
            exit_flag = 1

    if exit_flag == 1:
        break
    
    RB_point=pyautogui.center(RB_pos)
    click(RB_point[0]+rand_x, RB_point[1]+rand_y)
    click(RB_point[0]+rand_x, RB_point[1]+rand_y)
    time.sleep(0.1) #wait for confirm to appear
    
    timeout_start = time.time()
    while(time.time() < (timeout_start + timeout)):
        Confirm_pos=pyautogui.locateOnScreen('confirm_button.png', confidence=0.8)
        if (keyboard.is_pressed('q') == True):
            exit_flag = 1
            break
        if (Confirm_pos != None):
            #Confirm refresh
            Confirm_point=pyautogui.center(Confirm_pos)
            click(Confirm_point[0]+rand_x, Confirm_point[1]+rand_y)
            click(Confirm_point[0]+rand_x, Confirm_point[1]+rand_y)
            refresh_count=refresh_count+1
            break

    if exit_flag == 1:
        break
    
    time.sleep(0.5)

# End of script
time_ran = datetime.datetime.now()-start_datetime
time_ran_mins = round(time_ran.total_seconds()/60)

if (exit_flag == 1):
    sys.stderr.write(f'\n\nMacro has forcefully exited.\n')
else:
    sys.stderr.write(f'\n\nMacro has finished running.\n')
    
sys.stderr.write(f'Total time ran: {time_ran_mins} minutes and {time_ran.seconds % 60} seconds\n\n')
sys.stderr.write(f'Total times refreshed: {refresh_count} \nSkystones used: {refresh_count*3}\n\n')
sys.stderr.write(f'Covenant medals bought: {covenant_count*5} \nMystic medals bought: {mystic_count*50}\n\n')
sys.stderr.write(f'Total gold used: {covenant_count*184000 + mystic_count*280000}\n')

