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
    
#   2. Store a random number as the answer/solution.
    random_number = random.randrange(10)
    counter = 0
    guessed_number = 0
#   3. Continuously prompt the player for a guess.
    while True:
        counter += 1



        print("The random number is  {}:  ".format(random_number))
#     a. If the guess is greater than the solution, display to the player "It's lower".
        try:
            guessed_number = int(input("Please enter a number   "))
            
#             if (guessed_number > 10 ):
#               print("Please enter a positive number between 1 and 10, Thank you   ")    
        except UnboundLocalError:
            print(UnboundLocalError)
        except ValueError:
            print(ValueError)
        else: 
            if (guessed_number > random_number):
                print("It is lower.   ")
    #     b. If the guess is less than the solution, display to the player "It's higher".
            elif (guessed_number < random_number):
                print("It is higher.   ")

    #   4. Once the guess is correct, stop looping, inform the user they "Got it"
            elif (guessed_number == random_number):
                print("Got It   ")
    #      and show how many attempts it took them to get the correct number.
                print("It took you {}, attempts  ".format(counter))
                print ("The guessed number was  {},   ".format(guessed_number))
    #   5. Let the player know the game is ending, or something that indicates the game is over.
                print("This game is over, thank you for playing   ")
                break

            
# ( You can add more features/enhancements if you'd like to. )
 

# Kick off the program by calling the start_game function.
start_game()
