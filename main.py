import pyautogui
import time

time.sleep(5)

try:
    a = str(input("Word to spam: "))
    b = int(input("How much: "))

    for i in range(b):
        pyautogui.typewrite(a)
        pyautogui.press("enter")

except:
    print("error")

# time.sleep(5)

# f = open("text", "r")

# for word in f:
#     pyautogui.typewrite(word)
#     pyautogui.press("enter")
