n = 1313131345+1
tablica = [1]*n
j = 2
while (j<=n/2):
    for i in range(j+j,n,j):
        tablica[i] = 0
    j += 1
print(tablica)
