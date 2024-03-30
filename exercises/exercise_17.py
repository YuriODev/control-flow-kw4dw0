# Your solution to Exercise 17
verif = False
while not verif:
  num = input("Enter a 6-digit number: ")
  if len(num) == 6:
    try:
      int_num = int(num)
      verif = True
    except:
      pass

if (int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5])):
  print("Happy")
else:
  print("Ordinary")

