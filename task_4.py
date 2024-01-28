from datetime import datetime as dtdt, timedelta

def get_upcoming_birthdays(users):
    dict_with_dates_for_ones = {}
    current_day = dtdt.now().date()
    current_week_start = current_day - timedelta(days=current_day.weekday())  # Початок поточного тижня

    for user in users:
        birthday_day = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()

        formatted_date_birthday = dtdt(current_day.year, birthday_day.month, birthday_day.day).date()

        difference = formatted_date_birthday - current_day

        if 0 <= difference.days < 7 and formatted_date_birthday.weekday() in [0, 1, 2, 3, 4]:
            dict_with_dates_for_ones[user["name"]] = formatted_date_birthday.strftime("%Y.%m.%d")
        elif difference.days < 0 and formatted_date_birthday.weekday() not in [5, 6]:
            continue
        else:  # Якщо припало на суботу чи неділю
            days_until_monday = 7 - formatted_date_birthday.weekday()
            formatted_date_birthday += timedelta(days=days_until_monday)
            dict_with_dates_for_ones[user["name"]] = formatted_date_birthday.strftime("%Y.%m.%d")

    return dict_with_dates_for_ones

users = [
    {"name": "Tanya", "birthday": "1990.01.28"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Nina", "birthday": "1990.01.30"},
    {"name": "Alex", "birthday": "1990.01.31"},
    {"name": "Eva", "birthday": "1990.02.1"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(">>> Список привітань на цьому тижні:")
for name, congratulation_date in upcoming_birthdays.items():
    print(f"* {name}, {congratulation_date}")
