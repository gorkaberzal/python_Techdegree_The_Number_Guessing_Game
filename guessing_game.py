"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

# Import the random module.
import random

high_score = 0

def start_game():

    global high_score

    print("\n------------ Welcome to our Guessing game ------------")
    print("The the current high score is: {} ".format(high_score))
    random_number = random.randrange(1, 11)
    counter = 0
    while True:
        counter += 1
        try:
            guessed_number = int(input("Please enter a number between 1 and 10 "))
            if (guessed_number > 10 ) or (guessed_number < 1):
                print("You entered a non valid number outside the range.")
                continue
        except ValueError as e:
                print("You entered a non valid number between 1 and 10, {} ".format(ValueError))
                continue
        else: 
            if (guessed_number > random_number):
                print("It is lower.   ")
            elif (guessed_number < random_number):
                print("It is higher.   ")
            elif (guessed_number == random_number):
                print("\n--------------- Got It ----------------  ")
                print("It took you {}, attempts  ".format(counter))
                print ("The guessed number was  {}   ".format(guessed_number))
                if(high_score == 0) or (high_score >= counter):
                    high_score = counter
                play_again = input("Would you like to play agian (yes) / (no)   ")       
                if "yes" != (play_again.lower()):
                    print("This game is over, thank you for playing, goodbye  ")
                    break
                else:
                    start_game()

start_game()
