def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
print(recur_fibo(1))

#1 1 2 3 5 8 13 21 34