# Chapter 17 - PDF and Word Documents
# (Practice Program) - PDF Paranioa

import os, sys
import argparse
from PyPDF2 import PdfReader, PdfWriter, PasswordType
from pathlib import Path


def encrypt_pdf(path: str, password: str):
    reader = PdfReader(path)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    writer.encrypt(password)

    # Save the new PDF to a file
    filepath = path.removesuffix(".pdf") + "_encrypted.pdf"

    with open(filepath, "wb") as f:
        writer.write(f)

    return


def encrypt_pdfs(password: str, path: str='.'):
    for cwd, _, files in os.walk(path):
        for file in files:
            if str(file).endswith(".pdf"):
                p = Path(cwd, file)
                encrypt_pdf(path=str(p), password=password)


def decrypt_pdf(path: str, password: str):
    from PyPDF2 import PdfReader, PdfWriter

    reader = PdfReader(path)

    if reader.is_encrypted:
        result = reader.decrypt(password=password)
        
        if result == PasswordType.NOT_DECRYPTED:
            print("Incorrect password on file: " + path)
            return False

        writer = PdfWriter()

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Save the new PDF to a file
        filepath = path.removesuffix(".pdf") + "_decrypted.pdf"

        with open(filepath, "wb") as f:
            writer.write(f)

    return True


def decrypt_pdfs(password: str, path: str='.'):
    for cwd, _, files in os.walk(path):
        for file in files:
            if str(file).endswith(".pdf"):
                p = Path(cwd, file)
                decrypt_pdf(path=str(p), password=password)


def main():
    parser = argparse.ArgumentParser(
        description="Encrypt/Decrypt all pdfs in a folder."
    )
    
    # Add some positional arguments
    parser.add_argument("crypt", help="'e' or 'd' for encrypting/decrypting respectively")
    parser.add_argument("password", help="password (required)")
    parser.add_argument("path", nargs="?", default=None, help="An optional path to folder, otherwise cwd")

    # If no arguments given, print help
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    if args.crypt == "e":
        if args.path:
            encrypt_pdfs(password=args.password, path=args.path)
        else:
            encrypt_pdfs(password=args.password)
    elif args.crypt == "d":
        if args.path:
            encrypt_pdfs(password=args.password, path=args.path)
        else:
            encrypt_pdfs(password=args.password)
    else:
        raise Exception("Invalid argument for 'crypt', enter 'e' or 'd' for encrypting all files or decrypting them, respectively.")
    

if __name__ == "__main__":
    main()