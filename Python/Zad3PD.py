def nwd(x, y):
    if x < y:
        return nwd(y,x)
    if y ==0:
        return x
    return nwd(y,x % y)

najw = 0
lista = []
with open('liczby.txt', 'r') as plik:
    for rzad in plik:
        lista.append(int(rzad))

for i in range(200):
    opk = True
    for j in range(200):
        if i != j and nwd(lista[i], lista[j])>1:
            opk = False
    if (opk and lista[i] > najw):
        najw = lista[i]
print(najw)
