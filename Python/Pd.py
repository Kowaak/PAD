n = 100
i = 1
a = []
for i in range (n):
    a.append(i)
    i += 1
x = 2
w = a[0]
ilosc = 0
j = 1
for i in range (1,n):
        w = w * x +a[j]
        j = j + 1
        ilosc += j
print(w)
print(ilosc)
