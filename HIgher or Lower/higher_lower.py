import random
from art import logo, vs
from data import data


# getting random account:

def get_account():
    return random.choice(data)


# getting information of account :
def information(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


# checking who has more followers :

def greater(a_account , b_account):
    if a_account["follower_count"] > b_account["follower_count"]:
        return "a"
    else:
        return "b"


# Keeping track of scores :
def score(a):
    return a + 1


print(logo)
play = True
current_score = 0
while play:

    a_account = get_account()
    b_account = get_account()

    a_information = information(a_account)
    b_information = information(b_account)

    print(f"Compare A : {a_information}")
    print(vs)
    print(f"Compare B : {b_information}")

    guess = input("Who has more followers ? Type A or B :").lower()

    result = greater(a_account, b_account)

    if result == guess:
        current_score = score(current_score)
        print(f"You're Right ! Current Score = {current_score} ")
    else:
        print(f"Sorry , That's Wrong. Final score : {current_score}")
        play = False
