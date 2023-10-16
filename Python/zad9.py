import math
#A
x1 = float(input("Podaj x1: "))
y1 = float(input("Podaj y1: "))
x1 = abs(x1)
y1 = abs(y1)
#B
x2 = float(input("Podaj x2: "))
y2 = float(input("Podaj y2: "))
x2 = abs(x2)
y2 = abs(y2)
#P
x3 = float(input("Podaj x3: "))
y3 = float(input("Podaj y3: "))
x3 = abs(x3)
y3 = abs(y3)

d = math.sqrt((x2-x1)+(y2-y1))
e = 
print(d)
if(d/2):
    print("Punkt P jest srodkiem odcinka")
else:
    print("Punkt P nie jest srodkiem odcinka")

