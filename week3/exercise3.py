"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
  print("Welcome to the guessing game!")
  print("Please guess a number between _ and _?")
  lower_bound = input()
  upper_bound = input()

  while True:
    try:
      lower_bound = int(input("Enter a lower bound: "))
      upper_bound = int(input("Enter an upper bound: "))
      print("Great, a number between {lower} and {upper}.".format(lower = lower_bound, upper = upper_bound))
      break
    except:
      lower_bound = input("Enter a lower bound: ")
      upper_bound = input("Enter an upper bound: ")
      print("Please give me two numbers.")

  actual_number = random.randint(lower_bound, upper_bound)
  guess_number = input()
  guessed = False
  message = "Try to guess a number."
  
  while not guessed:
    print(message)
    try:
      guess_number = int(input(message))
      print ("Your guessed number is {}".format(guess_number))
      if guess_number == actual_number:
        print("You got it! It was {}".format(actual_number))
        guessed = True
      elif guessedNumber < actualNumber:
        print("Too small, try again :'(")
      else:
        print("Too big, try again :'(")

    except:
      guess_number = input(message)
      print("{} is not a number, please give me a number.".format(guess_number))

  return "You got it!"




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
