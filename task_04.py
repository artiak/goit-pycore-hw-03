from faker import Faker
from datetime import datetime


DATE_FORMAT = "%Y.%m.%d"


def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []

    cur_date = datetime.today().date()

    for user in users:
        birth_date = to_date(user["birthday"])
        greeting_date = to_greeting_date(birth_date, cur_date)
        
        remaining_days = (greeting_date - cur_date).days

        # current day plus 6 days
        if remaining_days > 6:
            continue

        weekday_idx = greeting_date.weekday()

        greeting_day = greeting_date.day

        # if birhtday is on Sunday, move to Monday
        if weekday_idx == 6:
            greeting_date = greeting_date.replace(day=greeting_day+1)

        # if birhtday is on Saturday, move to Monday
        if weekday_idx == 5:
            greeting_date = greeting_date.replace(day=greeting_day+2)

        upcoming_birthday = {
            "name": user["name"], "greeting_date": to_str(greeting_date)}

        upcoming_birthdays.append(upcoming_birthday)

    return upcoming_birthdays


def to_date(str_date: str):
    return datetime.strptime(str_date, DATE_FORMAT).date()


def to_greeting_date(birth_date, current_date):
    current_year = current_date.year

    greeting_date = birth_date.replace(year=current_year)

    if greeting_date < current_date:
        return greeting_date.replace(year=current_year + 1)

    return greeting_date


def to_str(datetime_date) -> str:
    return datetime_date.strftime(DATE_FORMAT)


# testing


users = [
    {"name": "John Early", "birthday": "1985.04.27"},
    {"name": "John Sunday", "birthday": "1985.05.11"},
    {"name": "John Saturday", "birthday": "1985.05.11"},
    {"name": "Jane Week", "birthday": "1990.05.17"},
    {"name": "Jane Late", "birthday": "1990.05.18"},
]

print(get_upcoming_birthdays(users))
