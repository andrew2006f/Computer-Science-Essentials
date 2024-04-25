# Single Player Guessing Game
# This game allows a player to guess a computer generated number

#IMPORTS
import random

#VARIABLES
userguess = -1
answer = -1
lives = 10

#BEGINNING OF GAME
print("Welcome to the Single Player Guessing Game!")
print("Guess a number between 1-100")

answer = random.randint(1, 100)
try:
    while(lives > 0):
        userguess = int(input("->"))
        print("You have guessed: ", userguess)
        lives -= 1
        print("You have", lives, "lives left")
        if userguess == answer:
            print("You Win")
            break
        elif userguess > answer:
            print("Guess Lower")
        elif userguess < answer:
            print("Guess Higher")
        else:
            print("Error has occured")
except:
    print("An error has occured, try again.")
print("Thanks for playing")
print("The secret number was ", answer)
