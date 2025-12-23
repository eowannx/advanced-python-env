#Assignment 2 - task 4
n, m = map(int, input().split())
text = input()
count = 0

for i in range(n - m + 1):
    tmp = text[i:i+m]
    unique = True
    for j in range(i):
        if text[j:j+m] == tmp:
            unique = False
            break
    if unique:
        count += 1

print(count)