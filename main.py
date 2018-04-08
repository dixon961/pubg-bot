import pyautogui
from time import sleep
from utils import *

print("Initializing bot...")
sleep(5)
while(True):
    start_pubg_game()
    sleep(3)
    press_button("f")
    sleep(2)
    exit_to_lobby()
    sleep(1)
    press_reconnect()