import os
import sys
import argparse
from practice.crypt import decrypt_pdf

DICTIONARY="dictionary.txt"

words = []


def collect_words():
    try:
        with open(os.path.join('automate_boring_stuff_files', DICTIONARY), 'r') as file:
            for word in file:
                words.append(word.strip())

        print(words)
    except FileNotFoundError:
        print('Dictionary file was not found.')
        sys.exit(1)


def brute_force(fp: str):
    for word in words:
        if decrypt_pdf(path=fp, password=word):
            return True
        elif decrypt_pdf(path=fp, password=str(word).upper()):
            return True
        
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Brute force decrypt a pdf file."
    )
    
    # Add some positional arguments
    parser.add_argument("filepath", help="File path of file to decrypt by brute force")
    collect_words()
    if brute_force(parser.filepath):
        print("Brute force was successful!")


if __name__ == "__main__":
    main()