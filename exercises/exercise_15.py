# Your solution to Exercise 15
verif = False
while not verif:
  day = int(input("Enter a day: "))
  if day > 0 and len(str(day)) in (1, 2):
    month = int(input("Enter a month: "))
    if month > 0 and len(str(month)) in (1, 2):
      year = int(input("Enter a year: "))
      if len(str(year)) == 4:
        verif = True


str_date_next = ""

if month in (1, 3, 5, 7, 8, 10, 12):
  if day != 31:
    str_date_next += f"{day+1}."
  else:
    str_date_next += "1."
    month += 1
elif month == 2:
  if day != 28:
    str_date_next += f"{day+1}."
  else:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
      str_date_next += f"{day+1}."
    else:
      str_date_next += "1."
      month += 1
else:
  if day != 30:
    str_date_next += f"{day+1}."
  else:
    str_date_next += "1."
    month += 1

if month < 13:
  str_date_next += f"{month}."
else:
  year += 1
  str_date_next += "1."

str_date_next += f"{year}"

print(str_date_next)
