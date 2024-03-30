# Your solution to Exercise 9
verif = False
while not verif:
  nums3 = int(input("Enter a 3-digit number: "))
  if len(str(nums3)) == 3:
    verif = True


nums3 = str(nums3)
cond1 = (int(nums3[0]) + int(nums3[2]) > int(nums3[1]))
cond2 = (int(nums3[0]) + int(nums3[2]) == int(nums3[1]))
cond3 = (int(nums3[0]) + int(nums3[2]) < int(nums3[1]))

print(">"*cond1+"="*cond2+"<"*cond3)
