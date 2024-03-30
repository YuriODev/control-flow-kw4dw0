# Your solution to Exercise 14
verif = False
while not verif:
  nums4 = input("Enter a 4-digit number: ")
  if len(nums4) == 4:
    verif = True
  try:
    int_nums4 = int(nums4)
  except:
    verif = False


print(nums4[0] == nums4[-1] and nums4[1] == nums4[-2])

