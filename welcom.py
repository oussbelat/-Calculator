print("Welcome")

num1 = float(input())
op = input()
num2 = float(input())

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Error: Dividing by 0 is not possible")
    else:
        print(num1 / num2)
elif op == "**":
    print(num1 ** num2)
else:
    print("Error: Invalid operation")