# Chapter 13 - Web Scraping
# (Project 6) - Run a Program with the webbrowser Module
# showmap.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip


def main():
    if len(sys.argv) > 1:
        # Get address from command line.
        address = ' '.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        address = pyperclip.paste()

    # Open the web browser.
    webbrowser.open('https://www.openstreetmap.org/search?query=' + address)


if __name__ == "main":
    main()