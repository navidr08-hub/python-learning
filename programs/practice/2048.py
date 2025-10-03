# Chapter 13 - Web Scraping
# (Practice Program) - 2048
# Windows 10 ONLY

import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # Setup Chrome with webdriver-manager (auto-installs correct driver)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Open the 2048 game
    driver.get("https://play2048.co/")

    time.sleep(2)  # wait for the game to load

    # Find the game container
    game_container = driver.find_element("tag name", "body")

    # Define possible moves
    moves = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

    # Play the game automatically
    while True:
        game_container.send_keys(random.choice(moves))
        time.sleep(0.1)  # adjust speed


if __name__ == "__main__":
    main()