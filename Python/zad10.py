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
#C
x3 = float(input("Podaj x3: "))
y3 = float(input("Podaj y3: "))
x3 = abs(x3)
y3 = abs(y3)

#AB = math.sqrt((x2-x1)+(y2-y1))
#BC = math.sqrt((x3-x2)+(y3-y2))
#AC = math.sqrt((x3-x1)+(y3-y1))
#obwod =  AB + BC + AC
pole = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)/2
print(pole)
