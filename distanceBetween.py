import math

def distanceBetween (x1,x2,x3,x4):
    distance = 0
    distance = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    return distance

x1 = int(input("Enter coordinate x frst point: "))
y1 = int(input("Enter coordinate y first point: "))
x2 = int(input("Enter coordinate x second point: "))
y2 = int(input("Enter coordinate y second point: "))
d = distanceBetween(x1, y1, x2, y2)

print("The distance is ", d)
