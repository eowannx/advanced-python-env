#Assignment 1 - task 4
N = int(input())
result = 0
step = 1 if N >= 1 else -1
for i in range(1, N + step, step):
    result += i
print(result)