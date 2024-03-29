# Your solution to Exercise 11
verif = False
while not verif:
  year = int(input("Enter a year: "))
  if 1900 <= year <= 3000:
    verif = True

cond1 = (year % 4 == 0)
cond2 = (year % 100 != 0)
cond3 = (year % 400 == 0)

if cond1 and cond2 or cond3:
  print("Leap year.")
else:
  print("Ordinary year.")
