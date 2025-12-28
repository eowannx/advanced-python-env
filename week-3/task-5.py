def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    numerator = A * D - C * B
    denominator = B * D
    common = gcd(abs(numerator), denominator)
    return numerator // common, denominator // common

A, B = map(int, input("Enter A/B: ").split('/'))
C, D = map(int, input("Enter C/D: ").split('/'))

num, den = subtract_fractions(A, B, C, D)
print(f"Subtraction (irreducible fraction): {num}/{den}")

N = int(input("Enter a number: "))
divisors = [i for i in range(1, N+1) if N % i == 0]
print("Divisors:", *divisors)