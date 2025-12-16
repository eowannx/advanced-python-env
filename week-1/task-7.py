#Assignment 1 - task 7
a = int(input("First number: "))
op = input("Operation: ")
b = int(input("Second number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Error")
else:
    print("Error")