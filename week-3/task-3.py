import math

def hypotenuse(a, b):
    return round(math.sqrt(a**2 + b**2), 2)

n1, n2 = map(int, input("Enter first legs: ").split())
n3, n4 = map(int, input("Enter second legs: ").split())

c1 = hypotenuse(n1, n2)
c2 = hypotenuse(n3, n4)

print("Hypotenuses:", c1, c2)
print("Greater hypotenuse:", max(c1, c2))
print("Smaller hypotenuse:", min(c1, c2))

def sort_letters(words):
    sorted_words = []
    for word in words:
        sorted_words.append(''.join(sorted(word)))
    return sorted_words

words = input().split()
sorted_words = sort_letters(words)
print("Sorted:", *sorted_words)