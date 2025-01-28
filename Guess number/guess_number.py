from art import logo
import random

print(logo)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
          22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
          41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
          60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
          79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
          98, 99, 100]

print("Welcome to the Number Guessing Game !")
print("I'm Thinking of a number between 1 to 100. ")
difficulty = input("Choose the difficulty . Type 'easy' or 'hard' : ").lower()
number = random.choice(numbers)

if difficulty == "easy":
    guesses = 10
    print(f"You have {guesses} attempt to guess the number.")
elif difficulty == "hard":
    guesses = 5
    print(f"You have {guesses} attempt to guess the number.")
else:
    print("Invalid choice!")

while guesses != 0:
    guess = int(input("Make a guess : "))

    if guess != number:
        guesses -= 1

    if guess == number:
        print(f"You got it ! The answer was {number}")
        exit()
    elif guess < number:
        print("Too low.")
        if guesses == 0:
            print("You've run out of guesses, You lose!")
            exit()
        print("Guess again.")
        print(f"You have {guesses} attempt remaining to guess the number.")
    elif guess > number:
        print("Too high.")
        if guesses == 0:
            print("You've run out of guesses, You lose!")
            exit()
        print("Guess again.")
        print(f"You have {guesses} attempt remaining to guess the number.")


