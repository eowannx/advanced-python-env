import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def quadrilateral_area(a, b, c, d, e):
    return triangle_area(a, b, e) + triangle_area(c, d, e)

A, B = map(int, input("Enter 2 numbers: ").split())
print("GCD:", gcd(A, B))
print("LCM:", lcm(A, B))

a, b, c, d, e = 3, 4, 5, 6, 5
print("Area:", quadrilateral_area(a, b, c, d, e))