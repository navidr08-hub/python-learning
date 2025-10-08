# Chapter 19 - Keeping Time, Scheduling Tasks, and Launching programs
# (Practice Program) - Monday the 14th Finder
# all_monday14.py - Finds all previous monday the 14th's until year 1

from datetime import datetime, timedelta


def all_monday14():
    current_day = datetime.now()
    one_day = timedelta(days=1)

    print("All previous Monday the 14th dates (back to year 1):\n")

    while current_day.year >= 1:
        if current_day.day == 14 and current_day.weekday() == 0:  # Monday == 0
            print(current_day.strftime("%B %d, %Y"))

        current_day -= one_day

        # Break manually when year 1 and day < 14 (to avoid negative years)
        if current_day.year == 1 and current_day.month == 1 and current_day.day == 1:
            break


def main():
    all_monday14()


if __name__ == "__main__":
    main()