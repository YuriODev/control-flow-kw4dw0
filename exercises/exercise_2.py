# Your solution to Exercise 2
age = int(input("Enter an age: "))

if age <= 1:
  print("You are an infant.")
elif 1 < age < 13:
  print("You are a child.")
elif 13 <= age < 20:
  print("You are a teenager.")
else:
  print("You are an adult.")
