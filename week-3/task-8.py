def div(n):
    r = []
    for num in range(1, n + 1):
        ok = True
        for d in str(num):
            d = int(d)
            if d == 0 or num % d != 0:
                ok = False
                break
        if ok:
            r.append(num)
    return r

def swap(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]

n = int(input())
nums = div(n)
print(*nums)

m = int(input())
A = list(map(int, input().split()))

swap(A)
print(*A)