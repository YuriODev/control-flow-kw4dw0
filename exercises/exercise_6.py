# Your solution to Exercise 6

x1 = int(input("Enter the x-coord of A: "))
y1 = int(input("Enter the y-coord of A: "))
x2 = int(input("Enter the x-coord of B: "))
y2 = int(input("Enter the y-coord of B: "))

Dist_A = (x1**2 + y1**2)**0.5
Dist_B = (x2**2 + y2**2)**0.5

if Dist_A > Dist_B:
    print("A is further from the origin.")
elif Dist_A == Dist_B:
    print("A and B are at the same distance from the origin.")
else:
    print("B is further from the origin.")
