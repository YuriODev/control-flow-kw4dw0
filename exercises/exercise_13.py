# Your solution to Exercise 13
verif = False
while not verif:
  nums4 = input("Enter a year: ")
  if len(nums4) == 4:
    verif = True
  try:
    int_nums4 = int(nums4)
  except:
    verif = False


counter = dict()
unique = True
for char in "0123456789":
  counter[char] = 0
  for num in nums4:
    if num == char:
      counter[char] += 1
      if counter[char] > 1:
        unique = False

print(unique)
