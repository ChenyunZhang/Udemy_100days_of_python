#Step 1 
import random

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

def guess_word():
    word_list = ["aardvark", "baboon", "camel"]
    rand = random.randint(0,2)
    chosen_word = word_list[rand]
    guess = input("Guess a letter: ")
    while not guess.isalpha():
        print("Input is invalid.")
        guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        return f"{guess} is in the {chosen_word}."
    else:
        return f"{guess} is not in the {chosen_word}."

print(guess_word())