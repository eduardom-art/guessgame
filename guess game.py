import random

print("Welcome to the Guessing Game!")

while True:
    secret_number = random.randint(1, 20)
    attempts = 5
    print("I am thinking of a number between 1 and 20.")
    print(f"You have {attempts} attempts left.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid number! Please enter a valid number.")
            continue

        if guess < 1 or guess > 20:
            print("Error! Try again with a number between 1 and 20.")
            continue

        if guess == secret_number:
            print("Congratulations! You won! 🎉")
            break
        
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        
        else:
            print("Too high! Try a lower number.")
        
        attempts -= 1

        if attempts > 0:
            print(f"Attempts left: {attempts}")
        else:
            print(f"Game Over! The number was {secret_number}. 💀")
            break

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            secret_number = random.randint(1, 20)
            attempts = 5
            print("Great! A new number has been generated. Let's play again!")
            print(f"You have {attempts} attempts left.")
            break
        elif play_again == "no":
            print("Thanks for playing! Goodbye! 👋")
            exit()
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")