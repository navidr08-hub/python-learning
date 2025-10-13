# Chapter 20 - Sending Emails, Texts and Push notifications
# (Practice Program) - Auto Unsubscriber
# Runs on Windows host machine with runnable browser

import ezgmail
import webbrowser
from bs4 import BeautifulSoup
import re


def get_unsubscribe_links():
    threads = ezgmail.search('unsubscribe')
    print('found', len(threads), 'unsubscribe emails...')

    unsubscribe_links = set()

    for thread in threads:
        for msg in thread.messages:
            matches = re.findall(r'https?://\S*unsubscribe\S*', msg.body)
            unsubscribe_links.update(matches)

    return list(unsubscribe_links)


def unsubscribe():
    links = get_unsubscribe_links()
    print(f"\nFound {len(links)} unsubscribe links.")
    if not links:
        print("No unsubscribe links found.")
        return

    for link in links:
        print(f"Opening: {link}")
        # webbrowser.open(link)


def main():
    unsubscribe()


if __name__ == "__main__":
    main()