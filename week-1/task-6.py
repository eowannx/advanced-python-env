#Assignment 1 - task 6
a = int(input("First number: "))
op = input("Operation: ")
b = int(input("Second number: "))

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b != 0:
        print(a/b)
    else:
        print("Error")
else:
    print("Error")