import math

def distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1)))

def radius(x1, y1, x2, y2):
    return distance(x1, y1, x2, y2)

def circumference(r):
    return 2 * 3.1416 * r

def area(r):
    return 3.1416 * r * r
    
x1 = int(input("Enter x1 for center: "))
y1 = int(input("Enter y1 for center: "))
x2 = int(input("Enter x2 for a point on circle: "))
y2 = int(input("Enter y2 for a point on circle: "))
r = radius(x1, y1, x2, y2)
print("Radius = ",r)
d = 2 * r
print("Diameter = ",d)
print("Circumference = ",circumference(r))
print("Area = ",area(r))
