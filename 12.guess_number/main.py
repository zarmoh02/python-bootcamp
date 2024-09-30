from art import logo
print(logo)
print("Welcome to GUESS A NUMBER! ")

import random

attempts = 0
difficulty = input("Choose a difficulty level. type 'Hard' or 'Easy': ").lower()
if difficulty == "hard":
    attempts += 5
elif difficulty == "easy":
    attempts += 7
#pick a random num:
random_num = random.randint(0,101)

is_winning = False

while is_winning == False or attempts != 0:
    guessed_num = int(input(f"you have {attempts} attempts, guess a number between(1,100) : "))
    if guessed_num > random_num:
        print("it's too high.")
        attempts -= 1
    elif guessed_num < random_num:
        print("it is too low.")
        attempts -= 1

    elif guessed_num == random_num:
        print("you've guessed the right number! congratulations!")
        is_winning = True

if attempts == 0 and is_winning == False:
    print(f"you've ran out of guesses:(. the number was {random_num}.")



