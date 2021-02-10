import pyautogui
import time

f = open("script.txt", "r")

for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")