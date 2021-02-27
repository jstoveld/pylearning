import random


def guessing_game():
    answer = random.randint(0, 100)
    too_high = 101
    too_low = -1

    while True:
        try:
            guess = int(input('What is your guess? '))
            if ValueError:
                guess = int(input('Guess must be a positive integer? '))
   
            if guess < too_high and guess > too_low:
                continue


        if guess is answer:
            print(f'Right!  The answer is {guess}')
            break

        elif guess < answer:
            print(f'Your guess of {guess} is too low!')
        elif guess > answer:
            print(f'Your guess of {guess} is too high!')
            


guessing_game()









# # Interact with the data and the user
#     while guess is not random_number:
#         if guess is type(int):
#             continue

#         if guess < random_number:
#             guess = int(input("Try again, but higher: "))
#             counter = counter+1
#             print("Your guess: " + str(guess))
#             print("Guess number " + str(counter))

#         if guess > random_number:
#             guess = int(input("Try again, but higher: "))
#             counter = counter+1
#             print("Your guess: " + str(guess))
#             print("Guess number " + str(counter))
        
#         elif guess == random_number:
#             print(f"Correct! The random number was: {guess}" )
#             print("Guess number " + str(counter))
#             break





