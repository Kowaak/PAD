a = [1,0,1,1,1,0,1]
x = 2
w = a[0]
i = 1
for i in range (1,len(a)):
        w = w * x +a[i]
        i = i + 1
print(w)
