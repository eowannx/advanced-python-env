#Assignment 1 - task 9
ticket = int(input())
a = ticket // 100000
b = (ticket // 10000) % 10
c = (ticket // 1000) % 10
d = (ticket // 100) % 10
e = (ticket // 10) % 10
f = ticket % 10
print("YES" if a + b + c == d + e + f else "NO")