#dozmiany = input('Podaj liczbe do zamiany: ')
def value(liczba):
    if (liczba == 'I'):
        return 1
    if (liczba == 'V'):
        return 5
    if (liczba == 'X'):
        return 10
    if (liczba == 'L'):
        return 50
    if (liczba == 'C'):
        return 100
    if (liczba == 'D'):
        return 500
    if (liczba == 'M'):
        return 1000
    else:
        print("Podaj prawidlowa liczbe")
        return -1
def zamiana(str):
    wynik = 0
    i = 0
    a = 0
    while (i < len(str)):
        string1 = value(str[i])
        if (i + 1 < len(str)):
            string2 = value(str[i + 1])
            if (string1 >= string2):
                wynik = wynik + string1
                i = i + 1
            else:
                wynik = wynik + string2 - string1
                i = i + 2
        else:
            a = a + string1
            i = i + 1
    return wynik
#print(zamiana(dozmiany)) 
print(zamiana("MMMCDI"))
