import random

random_number = random.randint(1, 100)
guesses = 0
user_guess = print("I'm thinking of a random number from 1 to 100.")
high_score = None # ChatGPT help

while True:
    try:
        if guesses == 0:
            try:
                user_guess = input("Take a guess! ")
                user_guess = int(user_guess)
                guesses += 1
                if user_guess == random_number:
                    print(f"Yay! You guessed it in {guesses} guesses!")
                    if guesses < high_score or high_score is None:
                        high_score = guesses
                        print(f"New high score: {high_score} guesses!")
                    else:
                        print(f"Your score of {guesses} is not better than the high score of {high_score}.")
                    print("Do you want to play again? (y/n)") # ChatGPT help
                    play_again = input()
                    if play_again == "y":
                        guesses = 0
                        random_number = random.randint(1, 100)
                    else:
                        break
                elif user_guess < random_number:
                    print("Too low.")
                    continue
                else:
                    print("Too high.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

        else:
            user_guess = input("Take another guess! ")
            user_guess = int(user_guess)
            guesses += 1
            if user_guess == random_number:
                print(f"Yay! You guessed it in {guesses} guesses!")
                if high_score is None or guesses < high_score:
                    high_score = guesses
                    print(f"New high score: {high_score} guesses!")
                else:
                    print(f"Your score of {guesses} is not better than the high score of {high_score}.")
                print("Do you want to play again? (y/n)")
                play_again = input()
                if play_again == "y":
                    guesses = 0
                    random_number = random.randint(1, 100)
                else:
                    break
            elif user_guess < random_number:
                print("Too low.")
                continue
            else:
                print("Too high.")
                continue
    except ValueError:
        print("Please enter a valid number.")
        continue
