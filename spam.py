import pyautogui
import time

limit = int(input("How many times u want to spam?"))
msg = input("Message wanna send?")

for i in range(limit): 
    pyautogui.typewrite(msg)
    pyautogui.press("Enter")


print('task completed')