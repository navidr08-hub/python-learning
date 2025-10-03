# Chapter 17 - PDF and Word Documents
# (Project 12) - Combine PDFs
# merge_pdfs.py - Combines PDFs into one pdf file
# WINDOWS 10 ONLY

import os
import sys
import glob
import PyPDF2

def merge_pdfs(pdf_list, output):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    with open(output, "wb") as f_out:
        merger.write(f_out)
    print(f"Merged {len(pdf_list)} PDFs into {output}")

if __name__ == "__main__":
    # Get path argument if provided, otherwise use cwd
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()

    # Expand to absolute path
    folder = os.path.abspath(folder)

    # Collect all PDFs in the folder
    pdf_files = sorted(glob.glob(os.path.join(folder, "*.pdf")))

    if not pdf_files:
        print("No PDF files found in:", folder)
        sys.exit(1)

    # Output filename
    output_file = os.path.join(folder, "merged.pdf")

    # Merge PDFs
    merge_pdfs(pdf_files, output_file)
