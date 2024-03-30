# Your solution to Exercise 4

num = int(input("Enter a grade: "))

if num in (1, 2, 3):
    print("initial level")
elif num in (4, 5, 6):
    print("average level")
elif num in (7, 8, 9):
    print("sufficient level")
elif num in (10, 11, 12):
    print("high level")
else:
    print("level is absent")
