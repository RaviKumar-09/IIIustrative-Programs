radius = float(input("Enter the radius"))
import math
pi = math.pi
areaCircle = pi*radius**2
print(areaCircle)
area = input('Enter the length and breath of a rectangle separated by spaces:')
length = float(area.split()[0])
breath = float(area.split()[1])
parameter = length*breath
print(parameter)