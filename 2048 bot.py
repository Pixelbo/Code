import pyautogui
import time

time.sleep(0.3)
def play2048(keys_combination):
    while True:
        for key in keys_combination:
            pyautogui.press(key)
            time.sleep(0.1)



play2048(['up', 'left', 'down', 'right']*20)