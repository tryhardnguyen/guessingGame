import random
from art import logo


def guessingGame(assignNumber):
    mode = input("Choose a difficulty. Type 'easy' or 'hard' \n")
    if mode == "easy":
        lives = 10
    if mode == "hard":
        lives = 5
    print(f"You have {lives} attempts remaining to guess the number")
    gamesRunning = True
    while gamesRunning:
        guess = int(input("Choose a number between 1 to 20 \n"))
        if guess > assignNumber:
            print("Too High")
            lives -= 1
            print(f"You have {lives} remaining lives")
            if lives == 0:
                print("You have no remaining lives")
                print("You lose")
                gamesRunning = False
        if guess < assignNumber:
            print("Too low")
            lives -= 1
            print(f"You have {lives} remaining lives")
            if lives == 0:
                print("You have no remaining lives")
                print("You lose")
                gamesRunning = False
        if guess == assignNumber:
            print("You win")
            gamesRunning = False


def game():
    print(logo)
    print("I'm thinking of a number between 1 and 20 \n")
    number = random.randint(1, 20)
    guessingGame(number)
    playAgain = input("Do you want play again? y/n \n")
    if playAgain == "y":
        game()

#Start the game
game()