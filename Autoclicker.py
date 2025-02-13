import keyboard
import pyautogui
import time
import threading

click_speed = 1/20 # Speed variable in miliseconds
clicking = False # Clicking status

# Function that executes an infinite loop that makes the clicking according to speed variable
def autoclick():
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(click_speed)

# Function that toggles the autoclick and executes it in the background
def toggle_autoclick():
    global clicking
    clicking = not clicking
    if clicking:
        threading.Thread(target=autoclick, daemon=True).start()
        
# Function to increase speed
def increase_speed():
    global click_speed
    click_speed = max(1/1000, click_speed - 1/200)
    print(str(click_speed))

# Function to decrease speed
def decrease_speed():
    global click_speed
    click_speed = min(1/2, click_speed + 1/200)
    print(str(click_speed))

keyboard.add_hotkey("ctrl+alt+m", toggle_autoclick) # Hotkeys to toggle autoclicking
keyboard.add_hotkey("shift+f", increase_speed) # Hotkeys to increase speed
keyboard.add_hotkey("shift+s", decrease_speed) # Hotkeys to decrease speed
keyboard.wait("esc") # Hotkey to exit the program