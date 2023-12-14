import re
import sys
import inflect

from datetime import date

date_regex = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
p = inflect.engine()

def main():

    inp = input("Date of Birth: ")

    minutes_old = convert_date_gap_to_minutes(inp)

    print(minutes_old)

def convert_date_gap_to_minutes(inp):

    if not re.search(date_regex, inp):
        sys.exit("Invalid date.")

    try:
        dob = date.fromisoformat(inp)
    except ValueError:
        sys.exit("Invalid date.")

    now = date.today()

    minutes_old = int((now - dob).total_seconds() / 60)

    return f"{p.number_to_words(minutes_old, andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
