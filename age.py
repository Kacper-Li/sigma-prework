# Take a date e.g(01-01-1990)
# Convert to a datetime object (date.fromisoformat)
# Get current date
# Calculate Difference
# Output number of years

from datetime import date

def age_calculator(date_given: date):
    current_date = date.today()
    difference = current_date - date_given
    years = difference.days // 365
    days = difference.days % 365
    nicer_output = f"{years} years and {days} days"
    return years

input_date = input("Enter a date in iso format|YYYY-MM-DD|: ")
formatted_date = date.fromisoformat(input_date)
time_difference = age_calculator(formatted_date)
print(f"{time_difference} years since {input_date}")
