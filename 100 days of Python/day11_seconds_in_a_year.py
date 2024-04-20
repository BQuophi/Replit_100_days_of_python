# How many seconds in a year 🙀 !! Day 11 of #Replit100DaysOfCode #100DaysOfCode. Join me on @Replit https://join.replit.com/python

print("Project Day : How many seconds are in a year?")
print()

print("There are 60 seconds in 1 minute")
print()
print("There are 60 minutes in 1 hour")
print()
print("There are 24 hours in 1 day")
print()
print("There are 365 days in 1 year")
print()
print("There are 366 days in a leap year")
print()

leap_year = input("Is it a leap year? ")
if leap_year == "yes" or leap_year == "Yes":
  print("There are 366 days in a leap year")
  print()
  leap_year = 366 * 24 * 60 * 60
  print("There are", leap_year, "seconds in a leap year")
  print("Do you also want to know how many seconds there are for non-leap years?")
  non_leap_year = input("Yes or No? ")
  if non_leap_year == "yes" or non_leap_year == "Yes":
    non_leap_year_seconds = 60 * 60 * 24 * 365
    print("There are", non_leap_year_seconds, "seconds in a non-leap year")
  elif non_leap_year == "no" or non_leap_year == "No":
    print("Okay, have a nice day!")
elif leap_year == "no" or leap_year == "No" :
  print("Then there are 365 days in the year")
  seconds_in_year = 60 * 60 * 24 * 365
  print("There are", seconds_in_year, "seconds in a year")

  
