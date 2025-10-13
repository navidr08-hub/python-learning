# Chapter 15 - Google Sheets
# (Practice Program) - Converting Spreadsheets to other formats
# Host machine only, requires browser
# For me: Ran on Windows host machine not WSL2

import os
import sys
import ezsheets
import argparse


def convert_sheets(directory, to: str):
    if not os.path.exists(directory):
        raise FileNotFoundError("Invalid path to directory")
    if not to in ['.xlsx', '.csv', '.ods', 'tsv']:
        raise NotImplementedError("Unsupported file type")
    for file in directory:
        if not str(file).endswith(('.xlsx', '.csv', '.ods', 'tsv')):
            continue
        ss = ezsheets.upload(file)
        if to == "excel":
            ss.downloadAsExcel()
        elif to == "csv":
            ss.downloadAsCSV()
        elif to == "html":
            ss.downloadAsHTML()
        elif to == "ods":
            ss.downloadAsODS()
        elif to == "pdf":
            ss.downloadAsPDF()
        elif to == "tsv":
            ss.downloadAsTSV()


def main():
    parser = argparse.ArgumentParser(
        description="Convert 'directory' of supported files 'to' specified file type"
    )
    
    # Add some positional arguments
    parser.add_argument("directory", help="Directory path of files to convert")
    parser.add_argument("to", help="Convert to which format? ('.xlsx', '.csv', '.ods', 'tsv')")

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    convert_sheets(args.directory, args.to)


if __name__ == "__main__":
    main()
