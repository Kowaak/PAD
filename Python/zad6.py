n = int(input("Podaj ilosc wyrazow: "))
s = 0
while(n>0):
    c = float(input("Podaj liczbe: "))
    if c >= 10:
        s = s + 1
    n = n - 1
else:
    print("Ilość wyrazów większych lub równych 10: ",s)
