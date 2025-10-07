# Chapter 15 - Google Sheets
# (Practice Program) - Finding Mistakes
# Host machine only, requires browser
# For me: Ran on Windows host machine not WSL2

import ezsheets


def mistakes_were_made():
    ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
    sheet = ss.sheets[0]

    mistakes = []

    for i in range(2, 15001):
        row =  sheet.getRow(i)
        beans, jars, total = int(row[0]), int(row[1]), int(row[2])
        if beans * jars != total:
            mistakes.append(i)
    
    return mistakes


def main():
    mistakes = mistakes_were_made()
    print(mistakes)


if __name__ == "__main__":
    main()