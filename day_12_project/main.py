# Number Guessing Game

from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
else:
    attempts = 5

SECRET_NUMBER = randint(1, 101)
continue_game = True

while attempts > 0:
    print(f"You have {attempts} remaining attempts to guess the number")
    guess = int(input("Make a guess: "))
    if guess == SECRET_NUMBER:
        print(f"You got it! The answer was {SECRET_NUMBER}.")
        break
    elif guess < SECRET_NUMBER:
        print("Too low.")
        attempts -= 1
    elif guess > SECRET_NUMBER:
        print("Too high.")
        attempts -= 1

    print("You have run out of guesses.")
