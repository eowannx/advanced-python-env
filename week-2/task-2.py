a = input()
b = input()
n = len(b)
bb = b + b
count = 0

for i in range(len(a) - n + 1):
    sub = a[i:i+n]
    if sub in bb:
        count += 1

print(count)