import math
#P
x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))
x1 = abs(x1)
y1 = abs(y1)
#S
x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))
x2 = abs(x2)
y2 = abs(y2)
r = math.sqrt(abs((x2-x1)+(y2-y1)))
print(r)
