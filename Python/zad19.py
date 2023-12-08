n = 5
t = [1]*(n+1)
i = 0
while(i<n):
    t[i] = int(input("Podaj liczbe do tablicy: "))
    i=i+1
k = i = 0
t[n-1] = int(input("Podaj wartownika: "))
#print(t)
while(i<n):
    if t[i] == t[n]:
        k = k + 1
    i = i + 1
print(k)
