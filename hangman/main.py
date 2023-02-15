import random
from hangman_art import *
from words_list import word_list


print(logo)

lives = 6
chosen_word = random.choice(word_list)
word_guess = []
wrong_letters = []
mistake = True

print(chosen_word)

## Display a "_" for each letter in the chosen_word
for item in range(len(chosen_word)):
    word_guess += "_"

while lives > 0:
    guess = str(input("\nPlease guess a letter: ")).lower()
    if len(guess) > 1 and not (guess.isalpha()):
        print("Your guess should be a letter only!")

    elif guess in wrong_letters or guess in word_guess:
        print("You've already tried that one, try again.")
    else:
        for letter in range(len(chosen_word)):
            if guess == chosen_word[letter]:
                mistake = False
                word_guess[letter] = guess
        if mistake == False:
            print("Good job!\nYour word: ")
            print(f"{' '.join(word_guess)}")
        elif mistake:
            if guess not in wrong_letters:
                lives -= 1
                print(stages[lives])
                wrong_letters += guess
                if lives == 0:
                    print("Sorry, you lost! You've no more tries.")
                elif lives > 0:
                    print("Sorry, you're wrong. You still have " + str(lives) + " lives")

    mistake = True
    if "_" not in word_guess:
        print("\n\nCongrats!! You won! \nYour word is: " + f"{''.join(word_guess)}")
        lives = 0 