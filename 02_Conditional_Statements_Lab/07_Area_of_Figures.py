import math

figure_type = input()

if figure_type == "square":
    side = float(input())
    square_area = side * side
    print(f"{square_area:.3f}")
elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    rectangle_area = side_b * side_a
    print(f"{rectangle_area:.3f}")
elif figure_type == "circle":
    circle_radius = float(input())
    circle_area = math.pi * circle_radius ** 2
    print(f"{circle_area:.3f}")
elif figure_type == "triangle":
    side = float(input())
    height = float(input())
    triangle_area = side * height / 2
    print(f"{triangle_area :.3f}")
