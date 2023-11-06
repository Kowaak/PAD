A = [2,2,2,2]
x = 2
n = len(A)
w = 0
mnozenia = 0
dodawania = 0
for i in range(n):
    potega = 1
    for j in range(i):
        potega *= x
        mnozenia += 1
    w = w + A[i] * potega
    if i > 0:
        dodawania += 1
print("Wynik:", w)
print("Ilość mnożeń:", mnozenia)
print("Ilość dodawań:", dodawania)
