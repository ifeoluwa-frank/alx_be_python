from datetime import datetime, timedelta

def display_current_datetime():
    today_date = datetime.now()
    current_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date


number_of_days = int(input("Enter number of days: "))

def calculate_future_date():
    additional_days = timedelta(days=number_of_days)
    future_date = datetime.now() + additional_days
    future_date = future_date.strftime("%Y-%m-%d")
    print(future_date)
    print(display_current_datetime())

calculate_future_date()