
import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You need to guess a randomly number within a chosen range.")
    
    start_bound = int(input("Enter the start point of the range: "))
    end_bound = int(input("Enter the end point of the range: "))
    if start_bound >= end_bound:
        print("end bound must be greater than start bound.")
        return
    
    target_number = random.randint(start_bound, end_bound)
    print(f"I've selected a random Number between {start_bound} and {end_bound}. Start guessing!!!!!!!!!!!!!!!!!")

    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < target_number:
            print("Too low!!!!!!!!!!Try again.")
        elif guess > target_number:
            print("Too high!!!!!!!!! Try again.")
        else:
            print(f"Congratulations!!!! You've guessed it {target_number} correctly in {attempts} attempts!")
            break


guessing_game()






