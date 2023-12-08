fib1 = 1
fib2 = 2
n = 5000
for i in range(2,n):
    a = fib1
    fib1 = fib2
    fib2 = a + fib2
    print(a)
    
    
