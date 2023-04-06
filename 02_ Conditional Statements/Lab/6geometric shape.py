import math

shape = input()  # read the shape from the user input

if shape == "square":
    side = float(input())  # read the side length from the user input
    area = side ** 2  # calculate the area of the square
elif shape == "rectangle":
    length = float(input())  # read the length from the user input
    width = float(input())  # read the width from the user input
    area = length * width  # calculate the area of the rectangle
elif shape == "circle":
    radius = float(input())  # read the radius from the user input
    area = math.pi * radius ** 2  # calculate the area of the circle using the math module
elif shape == "triangle":
    base = float(input())  # read the base from the user input
    height = float(input())  # read the height from the user input
    area = 0.5 * base * height  # calculate the area of the triangle
else:
    print("Invalid shape")  # print an error message if the input is not valid
    exit()
print('{:.3f}'.format(area))