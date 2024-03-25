# Your solution to Exercise 3

num = int(input("Enter a number: "))
if not (0 <= num <= 36):
  print("The bet will not play!")
else:
  if num == 0:
    print("Green")
  elif (1 <= num <= 10) or (19 <= num <= 28):
    print("Red") if num % 2 != 0 else print("Black")
  else:
    print("Black") if num % 2 != 0 else print("Red")
