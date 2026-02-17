# Take a date e.g(01-01-1990)
# Get current date
# Calculate Difference
# Output number of years

def age_calculator(date):
    current_date = "Feb 17 2026"
    difference = current_date - date
    whole_years = difference + " some logic that makes sure you count only full years"
    age = whole_years
    return age

input_date = input("Enter a date: ")
age_calculator(input_date)
