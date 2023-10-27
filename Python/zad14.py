import math
#algorytm ten stosujemy by zmniejszyc
#ilosc mnozen przy obliczniu wartosci wielomianu zmniejszamy tym zlozonosc obliczniowa
#jest to suma operacji arytmetycznych + porownania, czas wykonania programu
#zlozonosc powinna byc jak najmniejsza
#5x3 - 7x2 + 2x  - 3
#5*x*x*x - 7*x*x - 2*x - 3

n = int(input('Podaj n: '))
a = [5,7,-3]
x = int(input('Podaj x: '))
w = a[0]
i = 1
for i in a:
    if(i<=n):
        w = w * x +a[i]
        i = i + 1
print(w)
