"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730477669"

from string import whitespace

"""Establishs secret word and prompting user for a guess"""
word: str = "python"
length_word: int = len(word)

guess: str = input(f"What is your {length_word}-letter guess? ")
length_guess: int = len(guess)

"""Assigns unicode strings of the colored emoji boxes to variables. Emoji boxes indicate whether character in user's guess in secret word"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

"""Loop to ensure the user's guess is the same length as the secret word"""
while length_guess != length_word:
    guess = input(f"That was not {length_word} letters! Try again: ")
    length_guess = len(guess)

"""Loop to check if secret word and user's guess index characters match"""
i: int = 0
j: int = 0
wrong_position: bool = False
emoji_boxes: str = ""

while i < length_word:
    if guess[i] == word[i]:
        emoji_boxes += GREEN_BOX
    else:
        """Loop to check if character in user's guess is found anywhere in secret word"""
        j = 0
        wrong_position = False

        while j < length_word and wrong_position == False:
            if guess[i] == word[j]:
                wrong_position = True
            else:
                j += 1
                wrong_position = False
                
        if wrong_position == True:
            emoji_boxes += YELLOW_BOX
        else:
            emoji_boxes += WHITE_BOX
    i += 1

"""Displaying results of user's guess"""
if guess == word:
    print(emoji_boxes)
    print("Woo! You got it!")
else:
    print(emoji_boxes)
    print("Not quite. Play again soon!")
