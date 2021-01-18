import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def welcome():
    print(logo + "\n\n")
    difficulty = input("Welcome to the guessing game. Please choose the difficulty of the level (easy/hard):\n")
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def randomize():
    return random.randint(1, 101)



def guess(chosen_difficulty, number_to_be_guessed):
    guessed = False
    while(chosen_difficulty > 0):
        guess = int(input("Choose a number between 1 and 100\n"))
        if(guess > number_to_be_guessed):
            chosen_difficulty -= 1
            print(f"Too high. You have {chosen_difficulty} attempts left.\n")
        elif(guess < number_to_be_guessed):
            chosen_difficulty -= 1
            print(f"Too low. You have {chosen_difficulty} attempts left.\n")
        else:
            print("Nicely done, you've guessed it right!")
            guessed = True
            break
    
    print(f"The number to be guessed was {number_to_be_guessed}.")

    return guessed

play_again = 'y'
while(play_again == 'y'):
    chosen_difficulty = welcome()

    print(f"You have {chosen_difficulty} attempts to guess the number.\n")

    number_to_be_guessed = randomize()

    guess(chosen_difficulty, number_to_be_guessed)

    play_again = input("Do you want to play again (y/n)?\n")
