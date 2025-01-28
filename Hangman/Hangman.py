import random
from hangman_words import word_list
from art import logo, stages

print(logo)
end_of_game = False
word_list = word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if letter != guess:
        print(f"Entered letter '{guess}' is not in the word !")
        lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose !")
    if guess in display:
        print(f"you already guessed the letter '{guess}' ")
        lives
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])