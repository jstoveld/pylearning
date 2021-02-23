import random

def guessing_game():
    random_number = random.randint(1, 100)
    guess = int(input("Guess what the number is: "))
    if guess < 0:
        guess = int(input("Please type a positive integer: "))
    print("Your guess: " + str(guess))

    while True:
        if guess == random_number:
            print(f"Correct! The random number was: {guess}" )
            break

        if guess < random_number:
            guess = int(input("Try again, but higher: "))
        else:
            guess = int(input("Try again, but lower: "))
           


guessing_game()
