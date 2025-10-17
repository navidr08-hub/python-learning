# Chapter 23 - Controlling Keyboard and Mouse
# (Practice Program) - Reading Text Fields with Clipboard
# Windows 10 ONLY

"""
Write a program that follows this procedure for copying the text from a window’s text fields. 
but just pass it to print() for now.
Use pyautogui.getWindowsWithTitle('Notepad') (or whichever text editor you choose) 
to obtain a Window object. The top and left attributes of this Window object can tell you where this window is, 
while the activate() method will ensure that it is at the front of the screen. 
You can then click the main text field of the text editor by adding, 
say, 100 or 200 pixels to the top and left attribute values with pyautogui.click() 
to put the keyboard focus there. Call pyautogui.hotkey('ctrl', 'a') and 
pyautogui.hotkey('ctrl', 'c') to select all the text and copy it to the clipboard. 
Finally, call pyperclip.paste() to retrieve the text from the clipboard and paste it into your Python program. 
From there, you can use this string however you want, 

"""


import pyautogui
import pyperclip


WINDOW = 'Notepad'
MOUSE_POINT = (180, 160)


def copy_to_clipboard(window):
    win = pyautogui.getWindowsWithTitle(window)
    if win:
        win = win[0]
        win.activate()
        win.maximize()
        pyautogui.click(MOUSE_POINT[0], MOUSE_POINT[1], button='left')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        win.restore()
        win.minimize()
    else:
        print(f"No window with title {window}")


def read_text_from_clipboard(window):
    copy_to_clipboard(window)
    print(pyperclip.paste())
    powershell = pyautogui.getWindowsWithTitle('Windows Powershell')[0]
    powershell.activate()


def main():
    read_text_from_clipboard(WINDOW)


if __name__ == "__main__":
    main()