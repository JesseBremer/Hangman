import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
chosen_word = random.choice(word_list)
print(logo)
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"Oops you have already guess the letter: {guess}. Try a different letter!")
        guess = input("Guess a letter: ").lower()

    guessed_letters += guess
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed: {guess}. That's incorrect, you lose one life.")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The word you were trying to guess was: {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
