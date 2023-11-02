import math
n = int(input('Podaj n: '))
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
x = int(input('Podaj x: '))
w = a[0]
ilosc = 0
i = 1
for i in a:
    if(i<=n):
        w = w * x +a[i]
        i = i + 1
        ilosc += 1
print(w)
print(ilosc)
