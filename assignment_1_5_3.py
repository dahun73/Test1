def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

for i in range(1,11,1):
    print("a"+str(i),fib(i))
