from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    return age

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

age = calculate_age(birth_year, birth_month, birth_day)
print(f"You are {age} years old.")