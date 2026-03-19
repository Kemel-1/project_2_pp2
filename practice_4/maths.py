#1  convert degree to radian using the formula
# radian = degree × π / 180
import math
n=float(input())
print(n*math.pi / 180)

#2
# Calculate the area using the formula: (1/2) * (sum of bases) * height
a=int(input("Height: "))
b=int(input("Base, first value: "))
c=int(input("Base, second value:"))
print(((b+c)/2)*a)

#3
# Formula for area of a regular polygon:
# Area = (a * b^2) / (4 * tan(pi / a))
a=int(input("Input number of sides: "))
b=int(input("Input the length of a side: "))
S=(a*(b**2))/(4 * math.tan(math.pi / a))
print(S)

#4
# Calculate the area using the formula: area = base * height
a=int(input("Length of base: "))
h=int(input("Height of parallelogram: "))
print(a*h)