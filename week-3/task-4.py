def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def df(A, B, C, D):
    numerator = A * D
    denominator = B * C
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

def check(xc, yc, R, x, y):
    return (x - xc)**2 + (y - yc)**2 <= R**2

A, B = map(int, input("Enter A/B: ").split('/'))
C, D = map(int, input("Enter C/D: ").split('/'))

num, den = df(A, B, C, D)
print(f"irreducible fraction: {num}/{den}")

xc, yc, R = map(float, input("Enter x, y and radius: ").split())

points = []
for name in ['P', 'F', 'L']:
    x, y = map(float, input(f"Enter point {name}: ").split())
    points.append((x, y))

count = sum(check(xc, yc, R, x, y) for x, y in points)
print(f"Points inside the circle: {count}")