from time import sleep
import pyautogui

tbp = """
type anything here \n
"""

sleep(2)

pyautogui.write(tbp.replace("    ",""),interval=0.01)
