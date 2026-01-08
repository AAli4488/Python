#number guessing game by using random numbers
import random

lowest_num = 1
highest_num = 100
random_number = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python number guessing game!")
print(f"Guess a number between {lowest_num} and {highest_num}.")

while is_running:

    guess = input("Enter your guess (or 'q' to quit): ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"Please guess a number within the range of {lowest_num} to {highest_num}.")
        elif guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You've guessed the number {random_number} in {guesses} attempts.")
            is_running = False
    else:
        if guess.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            is_running = False
        else:
            print("Invalid input. Please enter a valid number or 'q' to quit.")        

   