# Chapter 8 - Strings and Text Editing
# (Project 2) - Add Bullets to Wiki Markup
'''bullet_point_adder.py - A script will get the text from the clipboard, 
add a star and space to the beginning of each line, and then paste this 
new text to the clipboard.'''

import pyperclip


def main():
    text = pyperclip.paste()

    # Separate lines and add stars.
    lines = text.split('\n')
    for i in range(len(lines)):  # Loop through all indexes in the "lines" list.
        lines[i] = '* ' + lines[i]  # Add a star to each string in the "lines" list.

    text = '\n'.join(lines)
    pyperclip.copy(text)


if __name__ == '__main__':
    main()
