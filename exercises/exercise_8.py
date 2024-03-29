# Your solution to Exercise 8
verif = False
while not verif:
  nums3 = int(input("Enter a 3-digit number: "))
  if len(str(nums3)) == 3:
    num = int(input("Enter a single digit: "))
    if len(str(num)) == 1:
      verif = True

print((str(num) in str(nums3)))
