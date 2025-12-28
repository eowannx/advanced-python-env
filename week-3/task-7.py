def right_triangle_area(a, b):
    return 0.5 * a * b

def rectangle_area(a, b):
    return a * b

x, y, z, t = map(float, input().split())
area = right_triangle_area(x, y) + rectangle_area(z, t)
print(area)

n = int(input())
print(format(n, "o"))