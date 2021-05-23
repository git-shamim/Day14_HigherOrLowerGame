
from art import logo, vs
from GameData import data
import random


def account_details(account):
    name = account["name"]
    desc = account["description"]
    country = account["country"]
    return "{0}, a {1}, from {2}.".format(name, desc, country)


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


print(logo)
score = 0
second_account = random.choice(data)
continue_game = True

while continue_game:
    first_account = second_account
    if first_account == second_account:
        second_account = random.choice(data)

    print("Compare A: {}.".format(account_details(first_account)))
    print(vs)
    print("Against B: {}.".format(account_details(second_account)))

    guess = input("Who has more Twitter followers? Type 'A' or 'B'. \n : ").lower()
    a_count, b_count = first_account["follower_count"], second_account["follower_count"]

    is_correct = check_answer(guess, a_count, b_count)
    if is_correct:
        score += 1
        print("You are right! Current score : {}.".format(score))
    else:
        print("Sorry, that's wrong. Final score : {}.".format(score))
        continue_game = False
