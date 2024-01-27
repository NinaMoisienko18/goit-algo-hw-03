from datetime import datetime as dtdt

def get_days_from_today(date):
    change_format = dtdt.strptime(date, "%Y-%m-%d")
    date_now = dtdt.now()
    difference = date_now.date() - change_format.date()
    return difference.days


date = input("Enter the date in YYYY-MM-DD format: ")
print(f"Count of days between your date and current day: {get_days_from_today(date)}")

