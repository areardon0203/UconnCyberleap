def f(n):
    if n == 3:
        return 1
    else:
        return f(n-1) + f (n-1)(n-2) // 2 
     


print(f(9))