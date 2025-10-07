# Chapter 15 - Google Sheets
# (Practice Program) - Download Google Forms Data
# Host machine only, requires browser
# For me: Ran on Windows host machine not WSL2

import ezsheets

def download_gform_data():
    ss = ezsheets.Spreadsheet("https://docs.google.com/spreadsheets/d/1kriuORiHm6jG5nUJFOBabHrhbxu1SjwZEB-No6XajCQ/edit?resourcekey=&gid=880335955#gid=880335955")
    sheet = ss.sheets[0]
    emails = sheet.getColumn(3)

    first_blank_index = emails.index('')
    # Slice the list up to that index
    emails_until_blank = emails[:first_blank_index]
    print(emails_until_blank)


def main():
    download_gform_data()


if __name__ == "__main__":
    main()
