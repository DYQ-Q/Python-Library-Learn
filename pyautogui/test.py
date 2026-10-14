import pyautogui

pyautogui.press('capslock')
pyautogui.write(
    'Hello',

    interval=0.1
)
pyautogui.press('capslock')

pyautogui.alert(
    'Hello'
)
pyautogui.hotkey(
    'ctrl',
    's'
)
#HelloHello
