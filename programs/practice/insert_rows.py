# Chapter 14 - Excel Spreadsheets
# (Practice Program) - Insert Blank Rows
# insert_rows.py - inserts N blank rows after specified row number M


import sys
import openpyxl
from openpyxl.utils.exceptions import InvalidFileException
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Insert N blank rows after specified row number M."
    )
    
    # Add some positional arguments
    parser.add_argument("N", type=int, help="Number of blank rows to insert")
    parser.add_argument("M", type=int, help="Row number to insert blank rows after")
    parser.add_argument("filepath", help="Excel filepath to insert blank rows into")

    if len(sys.argv) == 1 or len(sys.argv) > 4:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    try:
        wb = openpyxl.load_workbook(args.filepath)
    except (FileNotFoundError, InvalidFileException) as e:
        print(e)
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    ws = wb.active  # Get the active worksheet
    ws.insert_rows(args.N, amount=args.M)
    wb.save(filename=args.filepath)


if __name__ == "__main__":
    main()