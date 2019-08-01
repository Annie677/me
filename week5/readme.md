def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
print(recur_fibo(1))

#1 1 2 3 5 8 13 21 34

The first question repeated the "Get ready to strat in" and the only variables are the numbers. Therefore, a for loop will provide the numbers counting from 9 to 1. 
It will be easier to use a loop rather than repeating.

The "recursion" is about replacing the original characters into new items. Like the 
example of "italian_dinner" in the exercise2. 
So, if A is changed into "AB" and B is changed into "BA", then AB will return "ABBA".
Then, the "ABBA" is changed into "ABBABAAB"...