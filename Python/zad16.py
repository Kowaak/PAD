import time
start = time.time()
#biliard trzysta trzynaście bilionów sto trzydzieści jeden miliardów trzysta czterdzieści pięć milionów trzysta sześćdziesiąt cztery tysiące sto dwadzieścia trzy
liczba = 1313131345364123
def pierwsza(liczba):
    if liczba == 2:
        return "Tak"
    if liczba % 2 == 0 or liczba <=1:
        return "Nie"
    for dziel in range(3,int(liczba/2),2):
        if liczba % dziel == 0:
            return "Nie"
    return "Tak"
print(pierwsza(liczba))

end = time.time()
print(end - start)
