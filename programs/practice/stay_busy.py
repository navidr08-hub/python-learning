# Chapter 23 - Controlling Keyboard and Mouse
# (Practice Program) - Looking Busy
# stay_busy.py - Script to move mouse slightly evry 10s to not idle the computer screen
# Windows 10 ONLY


import pyautogui
import time


def stay_busy():
    try:
        while True:
            pyautogui.move(-1, 0, duration=1)  # Move left 1 pixel
            time.sleep(10)
            pyautogui.move(1, 0, duration=1)  # Move right 1 pixel
            time.sleep(10)
    except KeyboardInterrupt:
        print("Ended stay_busy.py program")
    
    return


def main():
    stay_busy()


if __name__ == "__main__":
    main()