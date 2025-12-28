import math

def triangle_area(base, height):
    return 0.5 * base * height

def hexagon_area(a):
    h = (math.sqrt(3) / 2) * a
    return 6 * triangle_area(a, h)

def rectangle_area(width, height):
    return width * height

a = float(input("Enter the side of the regular hexagon: "))
print("Area of the hexagon =", round(hexagon_area(a), 2))

for i in range(1, 4):
    w = float(input(f"Enter width of rectangle {i}: "))
    h = float(input(f"Enter height of rectangle {i}: "))
    print("Area =", round(rectangle_area(w, h), 2))