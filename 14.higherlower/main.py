from game_data import data
from art import logo , vs
import random

def random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    follower_count = account["follower_count"]
    description = account["description"]
    country = account["country"]
    return f"{name}, {follower_count}, {description}, {country}"

def check_answer(guess, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    game_over = False
    score = 0
    account_a = random_account()
    account_b = random_account()

    while not game_over:
        account_a = account_b
        account_b = random_account()
        if account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        guess = input("which one has more followers? type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        print(logo)

        if is_correct:
            score += 1
            print(f"you're right! your currennt score is {score}.")
        else:
            game_over = True
            print(f"Nope! your final score is {score}.")
game()

