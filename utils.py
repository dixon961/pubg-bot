import pyautogui
from time import sleep

screen_width, screen_height = pyautogui.size()

def start_pubg_game():
    move_mouse_to(screen_width * 0.1, screen_height * 0.95)
    press_LMB()

def exit_to_lobby():
    move_mouse_to(screen_width * 0.9, screen_height * 0.9)
    press_LMB()
    move_mouse_to(screen_width * 0.45, screen_height * 0.55)
    press_LMB()

def press_button(button):
    pyautogui.press(button)

def move_mouse_to(x, y):
    pyautogui.moveTo(x, y, duration = 0.25)

def press_LMB():
    pyautogui.click(button = 'left')

def press_RMB():
    pyautogui.click(button = 'right')