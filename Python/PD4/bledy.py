def funk(n, tab):
    ruz=[]
    for i in range(len(tab) - 1, 0, -1):
        r = tab[i] - tab[i - 1] 
        ruz.append(r)
    for i in range(len(ruz) - 1):
        if ruz[i] == ruz[i + 1]:
            return(ruz[i])
    if ruz[0] == ruz[len(ruz)-1]:
            return(ruz[0])

wynik = open('wynik3.txt','w')
with open('bledne.txt', 'r') as plik:
    for rzad in plik:
        linia = rzad.split()
        dlugosc = len(linia)
        if dlugosc>1:
            tab=[]
            for i in range(dlugosc):
                tab.append(int(linia[i]))
            reszta = funk(dlugosc, tab)

            tab2=[tab[0],tab[1],tab[2]]
            if tab2[1]-tab2[0]!=reszta and tab2[2]-tab2[1]==reszta:
                wynik.write(str(tab2[0])+"\n")
                
            for i in range(1,dlugosc-2):
                lewo = tab2[1]-tab2[0]
                prawo = tab2[2]-tab2[1]
                if reszta != lewo and reszta != prawo:
                    wynik.write(str(tab2[1])+"\n")
                tab2 = [tab[i],tab[i+1],tab[i+2]]
                
            if tab2[2]-tab2[1]!=reszta and tab2[1]-tab2[0]==reszta:
                wynik.write(str(tab2[2])+"\n")
wynik.close()
plik.close()