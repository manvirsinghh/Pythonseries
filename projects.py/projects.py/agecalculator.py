from datetime import datetime
def calculate_age():
  age=current_year-birth_year
  print(f"your age is:{age}")

print("Hi, you can find your current age here using age calculator")
birth_year=int(input("enter your birth year here:"))
# current_year=int(input("enter the current year here:")) we can import year along with datetime module to know current year instead of getting input of current year from user
current_year=datetime.now().year

calculate_age()

