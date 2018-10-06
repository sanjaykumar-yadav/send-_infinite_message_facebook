#! python3
import pyautogui, sys,time
pyautogui.hotkey("ctrl","altleft","f")
time.sleep(3)
pyautogui.moveTo(600, 106,3)
pyautogui.click()
pyautogui.typewrite("www.facebook.com",interval=0.25)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(1190, 751,3)
pyautogui.click()
pyautogui.typewrite("your friend name" , interval=0.25)
pyautogui.moveTo(1224, 721,3)
time.sleep(3)
pyautogui.click()
pyautogui.moveTo(926, 727,3)
pyautogui.click()
while(True):
	pyautogui.typewrite("message you want to send")
	pyautogui.press('enter')
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
