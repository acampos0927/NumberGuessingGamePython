import random
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if attempts == 10: 
        print(f"Game over! The correct number was {secret_number}.")
        break

    if guess < secret_number:
        print(f"Too low! Try between {guess} and 100.")
    elif guess > secret_number:
        print(f"Too high! Try between 1 and {guess}.")
    else: 
        print(f"Congratulations! You guessed the number in {attempts} attempts.")  
        break