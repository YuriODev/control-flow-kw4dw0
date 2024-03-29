# Your solution to Exercise 12
verif = False
while not verif:
  nums4 = int(input("Enter a year: "))
  if len(str(nums4)) == 4:
    verif = True

list_nums4 = list(str(nums4))

for i in range(len(list_nums4)):
  if int(list_nums4[i]) % 2 == 0:
    list_nums4[i] = "*"

str_nums4 = "".join(list_nums4)

print(str_nums4)
