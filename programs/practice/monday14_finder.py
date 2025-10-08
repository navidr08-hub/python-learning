# Chapter 19 - Keeping Time, Scheduling Tasks, and Launching programs
# (Practice Program) - Monday the 14th Finder
# monday14_finder.py - Finds the next 10 monday the 14th dates

from datetime import datetime, timedelta

def monday14_finder():
    current_day = datetime.now()
    one_day = timedelta(days=1)

    found = 0

    print("Next 10 Monday the 14th dates:\n")

    while found < 10:
        if current_day.day == 14 and current_day.weekday() == 0:  # Monday == 0
            print(current_day.strftime("%B %d, %Y"))
            found += 1

        current_day += one_day


def main():
    monday14_finder()


if __name__ == "__main__":
    main()