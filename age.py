# Take a date e.g(01-01-1990)
# Convert to a datetime object (date.fromisoformat)
# Get current date
# Calculate Difference
# Output number of years

from datetime import datetime, timedelta, date

def age_calculator(date_given: date):
    current_date = date.today()
    difference = current_date - date_given
    age = difference.days // 365
    return age

input_date = input("Enter a date in iso format|YYYY-MM-DD|: ")
formatted_date = date.fromisoformat(input_date)
print(formatted_date)
print(f"{age_calculator(formatted_date)} years since {input_date}")
