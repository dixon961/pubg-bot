import pyautogui
from time import sleep

screen_width, screen_height = pyautogui.size()

def start_pubg_game():
    move_mouse_to(131, 660)
    press_LMB()
    move_mouse_to(screen_width * 0.1, screen_height * 0.95)
    press_LMB()

def exit_to_lobby():
    move_mouse_to(screen_width * 0.9, screen_height * 0.9)
    press_LMB()
    move_mouse_to(screen_width * 0.45, screen_height * 0.55)
    press_LMB()

def press_reconnect():
    move_mouse_to(screen_width * 0.5, screen_height * 0.55)
    press_LMB()
    move_mouse_to(screen_width * 0.5, screen_height * 0.6)
    press_LMB()
    move_mouse_to(screen_width * 0.5, screen_height * 0.65)
    press_LMB()

def walk_forward():
    press_button("numlock")  

def is_in_airplane(image):
    point_one = image.getpixel((screen_width * 0.07, screen_height * 0.85)) == (255, 216, 0)
    point_two = image.getpixel((99, 710)) == (255, 216, 0)
    point_three = image.getpixel((87, 770)) == (255, 216, 0)
    point_four = image.getpixel((103, 797)) == (255, 216, 0)
    first = image.getpixel((screen_width * 0.07, screen_height * 0.85)) == (255, 216, 0)
    return point_one or point_two or point_three or point_four

def is_in_main_menu(image):
    return(image.getpixel((177, 40))) == (255, 199, 0)

def in_kill_screen(image):
    return(image.getpixel((81, 127))) == (248, 200, 0)

def in_reconnect_screen(image):
    return(image.getpixel((186, 824))) == (245, 203, 41)

def lay_down():
    pyautogui.press("z")

def leave_match():
    press_button('escape')
    sleep(1)
    move_mouse_to(714, 500)
    sleep(1)
    press_LMB()
    sleep(1)
    move_mouse_to(615, 475)
    sleep(1)
    press_LMB()

def press_button(button):
    pyautogui.press(button)

def move_mouse_to(x, y):
    pyautogui.moveTo(x, y, duration = 0.25)

def press_LMB():
    pyautogui.click(button = 'left')

def press_RMB():
    pyautogui.click(button = 'right')