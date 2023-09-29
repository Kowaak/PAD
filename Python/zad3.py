a = 1
b = 7
c = 3
x = 0
import math
w = abs(a-b)+math.sin(a)*math.sqrt(b)

if a%2 == 0:
    print("Liczba jest parzysta")
elif b==4:
    print("what")
else:
    print("Liczba jest nieparzysta")


delta = (b*b)-(4*a*c)
if delta > 0:
    print("Delta dodatnia")
    x1 = ((-1*b)-math.sqrt(delta))/(2*a)
    x2 = ((-1*b)+math.sqrt(delta))/(2*a)
    print(x1)
    print(x2)
elif delta == 0:
    print("Delta zero")
    x == (-1*b)/2 
    print(x)
else:
    print("Delta ujemna")
