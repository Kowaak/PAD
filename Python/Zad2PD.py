import math
dzielniki = 0
lista=[]
with open('liczby.txt','r') as plik:
    for rzad in plik:
        for i in range(1,int(rzad)):
            if int(rzad) % i == 0:
                dzielniki += 1
                lista.append(i)
        lista.append(int(rzad))
        dzielniki += 1
        if dzielniki == 18:
            print(rzad)
            print(lista)
        dzielniki = 0
        lista = []
