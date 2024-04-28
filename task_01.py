from datetime import datetime

def parse_date(in_date: str):
    date_format = '%Y-%m-%d'
    try:
        return datetime.strptime(in_date, date_format)
    except Exception:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format")

def get_days_from_today(date: str):
    parsed_date = parse_date(date)
    
    if not parsed_date:
        return
    
    cur_date = datetime.today()
    
    return (cur_date - parsed_date).days

# testing
while True:
    date_str = input("Enter a date (YYYY-MM-DD): ")
    print(f"Days difference: {get_days_from_today(date_str)}") 