x = 4
def fib(n):
    if (n<3):
        return 1
    else:        
        return(fib(n-1)+fib(n-2))
print("Ilość trutni w n pokoleniu: ",fib(x))
print("Ilość robotnic w n pokoleniu: ",fib(x+1))
print("Ilość przodków: ",fib(x+2))
