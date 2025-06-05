## creating a number guessing game
import random

number_to_guess = random.randint(1, 100)
max_number_of_guesses = 10
number_of_guesses = 0

print(f"I have chosen a number between 1 and 100, try to guess it you have {max_number_of_guesses} guesses to get it right!")

while number_of_guesses <= max_number_of_guesses:
    guess = int(input("Please enter a guess: "))
    number_of_guesses += 1
    if guess > number_to_guess:
        print(f"Too high! Guess again! You have {max_number_of_guesses - number_of_guesses} guesses left!")
    elif guess < number_to_guess:
        print(f"Too low! Guess again! You have {max_number_of_guesses - number_of_guesses} guesses left!")
    elif guess == number_to_guess:
        print("You guessed right! You guessed the number in", number_of_guesses, "guesses!")
        break
    else:
        print("Sorry, you ran out of tries better luck next time!")

