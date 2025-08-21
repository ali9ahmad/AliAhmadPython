##1.

from datetime import datetime

def calculate_age(birthdate):
  today = datetime.today()
  birthdate = datetime.striptime(birthdate, "%Y-%m-%d")

  years = today.year - birthdate.year
  months = today.month - birthdate.month
  days = today.day - birthdate.day

  if days < 0:
    months -=1
    days += (birthdate.replace(year = birthdate.year + 1, month+birthdate.month) - birthday).days

  if months < 0:
    year -= 1
    month += 12

  return year, months, days

def main():
  birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
  try:
    years, months, days = calculate_age(birthdate)
    print(f"You are {years} years, {months} months, and {days} days old")
  except ValueError:
    print("Please Enter a valid date in the format YYYY-MM-DD.")


if __name__ == "__name__"
  main()


##2.

from datetime import datetime, timedelta

def days_until_next_birthday(birthday):
  today = datetime.today()
  birthdate = datetime.strptime(birthday, "%Y-%m-%d")

  next_birthday = birthday.replace(year = today.year)

  if today > next_birthday:
    next_birthday = next_birthday.replace(year = today.year + 1)

  days_remaining = (next_birthday - today).days  
  return days_remaining

def main():
  birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
  try:
    days_remaining = days_until_next_birthday(birthday)
    print(f"There are {days_remaining} days until your next birthday.")
  except ValueError:
    print("Please enter a valid date in the format YYYY-MM-DD.")

if __name__ == "__main__"
  main()


##3.



