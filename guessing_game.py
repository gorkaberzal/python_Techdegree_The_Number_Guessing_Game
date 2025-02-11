"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

# Create the start_game function.
def start_game():
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
    print("Welcome to our Guessing game")
    guessed_number = print(input("Please enter a number   "))
#   2. Store a random number as the answer/solution.
    random_number = random(int)
#   3. Continuously prompt the player for a guess.
    while (random_number != guessed_number):
        attempts =+ 1
        guessed_number = int(input("Please enter a number   "))
#     a. If the guess is greater than the solution, display to the player "It's lower".
        if (guessed_number > random_number):
            print("It is lower.   ")
#     b. If the guess is less than the solution, display to the player "It's higher".
        elif (guessed_number < random_number):
            print("It is higher.   ")

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
    print("Got It   ")
#      and show how many attempts it took them to get the correct number.
    print("It took you {}, attempts  ".format(attempts))
#   5. Let the player know the game is ending, or something that indicates the game is over.
    print("This game is over, thank you for playing   ")
# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()
