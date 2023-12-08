n = 1000+1
tab = [1]*n
k = 2
while (k<n/2):
    for i in range(k+k,n,k):
        tab[i]=0
    k=k+1
for z in range(2,n):
    if tab[z]:
        print(z)
