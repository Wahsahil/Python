#Create a program of number guess game
import random
def guess_game():
    number = random.randint(1, 10)   
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("Too Low! Try again.")
        elif guess > number:
            print("Too High! Try again.")
        else:
            print("Correct! You guessed it right.")
guess_game()