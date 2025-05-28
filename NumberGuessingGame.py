import random
# Ask the user to choose difficulty
difficulty = input("Choose difficulty: Easy (E) or Hard (H): ").strip().upper()

# Set range & attempts based on difficulty
if difficulty == "E":
    max_number = 50
    max_attempts = 10
elif difficulty == "H":
    max_number = 100
    max_attempts = 5
else:
    print("Invalid choice, defaulting to Hard mode.")
    max_number = 100
    max_attempts = 5

# Generate secret number based on difficulty
secret_number = random.randint(1, max_number)
attempts = 0

while True:
    guess = int(input(f"Guess the number (between 1 and {max_number}): "))
    attempts += 1

    if attempts == max_attempts:  # End game if max attempts reached
        print(f"Game over! The correct number was {secret_number}.")
        break

    if guess < secret_number:
        print(f"Too low! Try between {guess} and {max_number}.")
    elif guess > secret_number:
        print(f"Too high! Try between 1 and {guess}.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")  
        break