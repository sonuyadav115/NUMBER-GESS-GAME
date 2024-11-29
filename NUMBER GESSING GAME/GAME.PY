import random

def guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # Randomly selecting a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    # Loop until the user guesses the number
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Start the game
guess_game()
