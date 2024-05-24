from datetime import date
from datetime import datetime
import inflect
import sys

def main():
    user_input= input("Date of Birth: ")
    get_minute= minutes(user_input)
    print(get_minute)

def minutes(user):
    p = inflect.engine()
    try:
        convert = datetime.strptime(user,"%Y-%m-%d").date()
        cal_dt=date.today()
        if convert > cal_dt:
           sys.exit("Birth date cannot be in the future.")
        difference = cal_dt - convert
        total = difference.days * 1440
        words = p.number_to_words(total,andword="")
        capitalize_word = words.capitalize()
        return f"{capitalize_word} minutes"
    except ValueError:
        sys.exit("Invalid Date Format")

if __name__ == "__main__":
    main()



