# Your solution to Exercise 16
verif = False
while not verif:
  day = int(input("Enter a day: "))
  if day > 0 and len(str(day)) in (1, 2):
    month = int(input("Enter a month: "))
    if month > 0 and len(str(month)) in (1, 2):
      year = int(input("Enter a year: "))
      if len(str(year)) == 4:
        verif = True

str_date_prev = ""

if day == 1:
  if month > 1:
    month -= 1
  else:
    month = 12
    year -= 1
  if month in (1, 3, 5, 7, 8, 10, 12):
    str_date_prev += "31."
  elif month == 2:
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
      str_date_prev += "29."
    else:
      str_date_prev += "28."
  else:
    str_date_prev += "30."
else:
  str_date_prev += f"{day - 1}."

str_date_prev += f"{month}.{year}"
print(str_date_prev)
