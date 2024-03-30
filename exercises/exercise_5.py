# Your solution to Exercise 5

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == b == c == 0:
    print("Infinite roots.")

elif a == 0:
    print(b/-c)

else:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("No roots.")
    elif discriminant == 0:
        print(-b/(2*a))
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f"{round(root1, 2)} and {round(root2, 2)}")
        
