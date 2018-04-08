import pyautogui
from time import sleep
from utils import *

print("Initializing bot...")
sleep(5)
while(True):
    print(pyautogui.position())
    image = pyautogui.screenshot()
    if (is_in_airplane(image)):
        print("I'm in airplane")
        sleep(40)
        press_button("f")
        sleep(90)
        walk_forward()
        sleep(190)
        leave_match()
    if (is_in_main_menu(image)):
        print("I'm in main menu")
        start_pubg_game()
        sleep(25)
    if (in_kill_screen(image)):
        print("I'm in kill screen")
        exit_to_lobby()
        sleep(10)
    if (in_reconnect_screen(image)):
        print("I'm in recconnect screen")
        press_reconnect()