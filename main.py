import random

random_number = random.randint(1, 100)
guesses = 0
user_guess = print("I'm thinking of a random number from 1 to 100.")

while True:
    if guesses == 0:
        user_guess = input("Take a guess! ")
        user_guess = int(user_guess)
        guesses += 1
        if user_guess == random_number:
            print("You guessed it!")
            break
        elif user_guess < random_number:
            print("Too low.")
            continue
        else:
            print("Too high.")
            continue
    else:
        user_guess = input("Take another guess! ")
        user_guess = int(user_guess)
        guesses += 1
        if user_guess == random_number:
            print(f"Yay! You guessed it in {guesses} guesses!")
            break
        elif user_guess < random_number:
            print("Too low.")
            continue
        else:
            print("Too high.")
            continue