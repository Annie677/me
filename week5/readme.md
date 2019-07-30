def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
print(recur_fibo(1))

#1 1 2 3 5 8 13 21 34

The first question repeated the "Get ready to strat in" and the only variables are the numbers. Therefore, a for loop will provide the numbers counting from 9 to 1. 

It will be easier to use a loop rather than repeating.