import pyautogui
import os
def take_screenshot():
    try:
        os.remove("image.png")
    except:
        pass
    pyautogui.screenshot("image.png")
    image = open("image.png", "rb")
    return image