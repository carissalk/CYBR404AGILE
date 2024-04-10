import time
import pyautogui

time.sleep(3)
file_name = "food.txt"
file = open(file_name, "r")
for line_num in file:
    text = file.readline()
    pyautogui.typewrite(text)
    time.sleep(1)
