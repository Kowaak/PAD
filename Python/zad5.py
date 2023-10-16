print("Podaj ilość elementów: ")
n = input()
n = int(n)
a = 0
suma = 0

for i in range (n,0,-1):
    print("Podaj liczbe do dodania: ")
    a = input()
    a = int(a)
    suma = suma + a
print("Suma wynosi: ",suma)


print("Podaj ilość elementów: ")
n = input()
n = int(n)
a = 0
suma = 0

for i in range (n,0,-1):
    print("Podaj liczbe do dodania: ")
    a = input()
    a = int(a)
    if a%2==0:
        suma = suma + a
print("Suma wynosi: ",suma)
