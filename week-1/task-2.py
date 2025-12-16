#Assignment 1 - task 2
a, b, c = map(int, input().split())
maximum = max(a, b, c)
minimum = min(a, b, c)
print(maximum - minimum)