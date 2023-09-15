import pyautogui
pyautogui.FAILSAFE = True
screenWidth, screenHeight = pyautogui.size()

# Play game (https://aimtrainer.io/challenge)
try:
    while True:
        cords = pyautogui.locateCenterOnScreen("targets.png", confidence=0.85)
        if cords != None:
            pyautogui.moveTo(cords)
            pyautogui.leftClick()
except (KeyboardInterrupt) as error:
    print(error)
