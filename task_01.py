from datetime import datetime


def get_days_from_today(date_str: str) -> int:
    in_date = parse_date(date_str)
    
    if (not in_date):
        return None
    
    cur_date = datetime.today()

    return (cur_date - in_date).days

def parse_date(date_str: str) -> datetime:
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except Exception:
        print("Invalid date format. Expected 'YYYY-MM-DD'")

        return None


# testing


while True:
    date_str = input("Enter a date (YYYY-MM-DD): ")
    date_diff = get_days_from_today(date_str)

    print(f"Days difference: {date_diff}")
