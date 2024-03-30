# Your solution to Exercise 7

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
operation = input("Enter a symbol: ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/" or "div":
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 / num2) if symbol == "/" else print(num1 // num2)
elif operation == "mod":
    print(num1 % num2)
elif operation == "pow":
    print(num1 ** num2)
