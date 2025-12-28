import math

def square_area(a):
    return round(a ** 2, 2)

def rectangle_area(b, h):
    return round(b * h, 2)

def parallelogram_area(b, h):
    return round(b * h, 2)

def rhombus_area(p, q):
    return round(0.5 * p * q, 2)

def trapezoid_area(a, b, h):
    return round(0.5 * (a + b) * h, 2)

def circle_area(r):
    return round(math.pi * r ** 2, 2)

def ellipse_area(a, b):
    return round(math.pi * a * b, 2)

def right_triangle_area(b, h):
    return round(0.5 * b * h, 2)

def triangle_area(b, h):
    return round(0.5 * b * h, 2)

def equilateral_triangle_area(b):
    return round((math.sqrt(3) / 4) * b ** 2, 2)

def array_stats(arr):
    total = sum(arr)
    average = round(total / len(arr), 2)
    return total, average


areas = [
    square_area(5),
    circle_area(3),
    rectangle_area(4, 6),
    ellipse_area(3, 2),
    parallelogram_area(5, 3),
    right_triangle_area(4, 5),
    rhombus_area(4, 6),
    triangle_area(4, 5),
    trapezoid_area(3, 5, 4),
    equilateral_triangle_area(6)
]

arrays = [
    [3, 7, 11, 19, 23],
    [5, 17, 29, 41],
    [2, 4, 8, 16, 32, 64]
]

stats_results = [array_stats(a) for a in arrays]

print("Areas:", areas)
print("Sum and average:", stats_results)