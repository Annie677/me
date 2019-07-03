"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
  print("Welcome to the guessing game!")
  print("Please guess a number between _ and _?")
  lower_bound = input()
  upper_bound = input()
  actualNumber = input()
  actualNumber = random.randint(lower_bound, upper_bound)
  guessed = False
  guess_number = input()
  while True:
    guess_number = input()
    try:
      lower_bound = int(input("Enter a lower bound: "))
      upper_bound = int(input("Enter an upper bound: "))
      if lower_bound < upper_bound:
        print("Great, a number between {lower} and {upper}.".format(lower = lower_bound, upper = upper_bound))
        try:
          guess_number = int(input("Guess a number: "))
          while True:
            guess_number = int(input("Guess a number: "))
            print("Your number is {},".format(guess_number))
            if guess_number == actualNumber:
              print("You got it! It was {}".format(actualNumber))
              return "You got it!"
            elif guess_number < actualNumber:
              print("Too small. Please try again.")
              
            if guess_number > actualNumber:
              print("Too big.Please try again.")
          
        except:
          guess_number = input("Guess a number:")
      else:
        print("Sorry, please try again.")
    except ValueError:
      print("Please give me two numbers.")
  
  
  
  

  




  """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    #return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
