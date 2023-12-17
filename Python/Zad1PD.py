file ='dane_wynik.txt'
f = open(file, 'r+')
w=0
with open('liczby.txt', 'r') as plik:
    for rzad in plik:
        if int(rzad) % 2==0:
            w+=1
print(w)
f.write(str(w))
f.close()
