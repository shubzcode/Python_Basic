# Python program to find Area of a circle using inbuild library
import math

def area(r):
  area = math.pi * r ** 2
  return area

radius = 3

area_of_circle = area(radius)

print("The area of the circle is:", area_of_circle)