import re
from datetime import datetime as dtdt

def get_days_from_today(date):
    change_format = dtdt.strptime(date, "%Y-%m-%d")
    date_now = dtdt.today()
    difference = date_now.date() - change_format.date()
    return difference.days


while True:
    date = input(">>> Enter the date in YYYY-MM-DD format: ")
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    if re.match(date_pattern, date):
        try:
            print(f"Count of days between your date and current day: {get_days_from_today(date)}")
            break
        except ValueError:
            print(f"Date not valid.")
            users_answer = input("You can try again\n1. Try again\n2. Exit\n>>>Your answer: ")
            if users_answer == "2":
                print("Bye!")
                break

    else:
        users_answer = input("Sorry.Date doesn't match pattern. You can try again\n1. Try again\n2. Exit\n>>>Your answer: ")
        if users_answer == "2":
            print("Bye!")
            break




