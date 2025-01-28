from art import logo
import random

want_play = "y"
while want_play == "y":
    want_play = input("Do you want to play a game of BlackJack ? Type 'y' or 'n' : ").lower()
    if want_play == "y":

        print(logo)


        def choice_card():
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            return random.choice(cards)


        def score(card_list):

            sum = 0
            for i in card_list:
                sum += i

            if 11 in card_list and sum > 21:
                card_list.remove(11)
                card_list.append(1)
                score(card_list)
            elif sum > 21:
                if card_list == user_cards:
                    print("You lose !! \n Because your score is above 21.")
                    print(f"Your final hand : {card_list}, Current score : {sum}")
                    exit()
                else:
                    print("You Won 🥳")
                    print(f"Computer's card : {card_list}, Current Score : {sum}")
                    exit()
            return sum


        play = True

        while play:

            user_cards = []
            for i in range(2):
                n = choice_card()
                user_cards.append(n)
            user_sum = score(user_cards)

            computer_cards = []
            for i in range(2):
                n = choice_card()
                computer_cards.append(n)
            computer_sum = score(computer_cards)

            print(f"Your cards : {user_cards}, Current score is : {user_sum}")
            print(f"Computer's first card : {computer_cards[0]}")
            choose = "y"
            while choose == "y":
                choose = input("Type 'y' to get another card, Type 'n' to pass : ").lower()
                if choose == "y":
                    a = choice_card()
                    user_cards.append(a)
                    user_sum = score(user_cards)
                    b = choice_card()
                    computer_cards.append(b)
                    print(f"Your cards : {user_cards}, Current score is : {user_sum}")
                    print(f"Computer's first card : {computer_cards[0]}")
                elif choose == "n":
                    if computer_sum < 21:
                        b = choice_card()
                        computer_cards.append(b)
                        computer_sum = score(computer_cards)
                    if user_sum > computer_sum:
                        print("You Win 🥳")
                        print(f"Your final hand : {user_cards}, Current score is : {user_sum}")
                        print(f"Computer final hand : {computer_cards}, Current score is : {computer_sum}")
                        play = False
                    elif user_sum == computer_sum:
                        print("Draw 😉")
                        print(f"Your final hand : {user_cards}, Current score is : {user_sum}")
                        print(f"Computer final hand : {computer_cards}, Current score is : {computer_sum}")
                        play = False
                    else:
                        print("You lose ☹")
                        print(f"Your final hand : {user_cards}, Current score is : {user_sum}")
                        print(f"Computer final hand : {computer_cards}, Current score is : {computer_sum}")
                        play = False
                else:
                    print("Invalid input !!")

    elif want_play == "n":
        exit()
    else:
        print("Invalid input !!")
