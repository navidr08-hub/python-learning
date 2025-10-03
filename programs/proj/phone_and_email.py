# Chapter 9 - Regular Expressions
# (Project 3) - Extract Contact Information from Large Documents
# phone_and_email.py - Extracts contact information for clipboard and copies it to the clipboard
'''To test your program, open your web browser to the No Starch Press contact page 
at https://nostarch.com/contactus press CTRL-A to select all the text on the page, 
and press CTRL-C to copy it to the clipboard. When you run this program, the output should 
look something like this:

Copied to clipboard:
800-555-7240
415-555-9900
415-555-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com
'''

import pyperclip, re


def main():
    phone_re = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  # Area code
        (\s|-|\.)?  # Separator
        (\d{3})  # First three digits
        (\s|-|\.)  # Separator
        (\d{4})  # Last four digits
        (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
        )''', re.VERBOSE)

    # Create email regex.
    email_re = re.compile(r'''(
    ❶ [a-zA-Z0-9._%+-]+  # Username
    ❷ @  # @ symbol
    ❸ [a-zA-Z0-9.-]+  # Domain name
        (\.[a-zA-Z]{2,4})  # Dot-something
        )''', re.VERBOSE)

    # Find matches in clipboard text.
    text = str(pyperclip.paste())

    matches = []
    for groups in phone_re.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[6] != '':
            phone_num += ' x' + groups[6]
        matches.append(phone_num)
    for groups in email_re.findall(text):
        matches.append(groups)

    # Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


if __name__ == '__main__':
    main()