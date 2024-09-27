from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date


number_of_days = int(input("Enter number of days: "))

def calculate_future_date():
    additional_days = timedelta(days=number_of_days)
    future_date = display_current_datetime() + additional_days
    print(future_date)

calculate_future_date()