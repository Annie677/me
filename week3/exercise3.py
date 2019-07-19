"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    while True:
        try:
            your_input = int(input(message))
            print("Thank you, {} is a number.".format(your_input))
            return your_input
        except:
            print ("that is not a number. Please try again.")


def advancedGuessingGame():
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
  print("Welcome to the guessing game!")
  print("Please guess a number between _ and _?")

  lower_bound = not_number_rejector("Enter a lower bound: ")
  upper_bound = not_number_rejector("Enter an upper bound: ")
  while lower_bound >= upper_bound:
      lower_bound = not_number_rejector("Enter a lower bound: ")
      upper_bound = not_number_rejector("Enter an upper bound: ")

  print("Great, a number between {lower} and {upper}.".format(lower=lower_bound, 
                                                              upper=upper_bound))
  guess_number = not_number_rejector("Guess a number: ")
  actualNumber = random.randint(lower_bound, upper_bound)
  while True:
    print("Your number is {},".format(guess_number))
    if guess_number == actualNumber:
      print("It was {}".format(actualNumber))
      return "You got it!"
    elif guess_number < actualNumber:
      print("Too small. Please try again.")
      guess_number = not_number_rejector("Guess a number: ")
    if guess_number > actualNumber:
      print("Too big.Please try again.")   
      guess_number = not_number_rejector("Guess a number: ")      


if __name__ == "__main__":
    print(advancedGuessingGame())
