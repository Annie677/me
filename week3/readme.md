Week 3:
'While' loop is able to run a command as a prerequisite. 
I think that the "range" is much more easier to return the expected results than the "while loop" in the exerise1. 
range (start, stop, step) is able to provide the needed items from the "beginning" to the "ending" with the expected steps. 
HOWEVER, the loops are more complicated to return the same list that I have to write " my_number += step" and define the "my_number" in the loop. 

In the guessing game "stubborn_asker", I created a while loop to ask the number, but it does not work. 

"def stubborn_asker(low, high):
    answer = int(input(question))
    question = "Please try to guess a number between {0} and {1}, Your number is {2}.".format(low, high, answer)
    while True:
        print(question)
        if low < answer < high:
            print ("That's right.")
            return answer
        else:
            print("Please try again.")"

I realize that the output for this while loop only ask the same question with same numbers over and over again. Is this because that the input number is not inside of the loop? 
Therefore I try to separate the question and "Your number is" into two parts. 
"while True:
      message = "your number is {}".format (answer)        
      answer = int (input(message))" 
Therefore, the given answer will change still the number is fit. 

In the question "not_number_rejector", I tried to use the "isdigit()" to decide if the input answer is a number or not. 
"if your_input.isdigit():
            print ("Thank you.{} is a number".format(answer))"
However, the answer input was a list and it shows an error:
"exception: 'list' object has no attribute 'isdigit'". 
So I try to use the "try except" to decide whether the input is a number or not. 

In the exercise2, there is a completed guessing game. 
“import random" and "randomint()" are able to create a random number.

In the exercise4, the binary_search is a way for picking up the right number faster. The binary search will divide the number list into two parts, then it will looking up the right number in the "low part" or "high part". If the right number is higher than the middle number, then it will use the "high part" which is faster and easier than looking up the number in the whole list. 

