"""EX03 - Structured Wordle."""

__author__ = "730477669"


def contains_char(searched_str: str, letter_guess: str) -> bool:
    """Given 2 strings, search the first string for the character in the second string, returning True if found."""
    # Ensure that the second parameter is only one character long.
    assert len(letter_guess) == 1

    # Loop to check if character in user's guess (letter_guess) is found anywhere in secret word (searched_str).
    j: int = 0
    length_word: int = len(searched_str)

    while j < length_word:
        if letter_guess == searched_str[j]:
            return True
        else:
            j += 1 

    return False


def emojified(word: str, guess: str) -> str:
    """Given two strings, display how closely guess resembles secret in emoji boxes."""
    # Ensure that the two parameters are the same length.
    assert len(guess) == len(word)

    """Assigns unicode strings of the colored emoji boxes to variables. Emoji boxes indicate whether character in user's guess in secret word."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # Loop to check if secret word and user's guess index characters match; adds corresponding emoji boxes.
    i: int = 0
    emoji_boxes: str = ""

    while i < len(word):
        if guess[i] == word[i]:
            emoji_boxes += GREEN_BOX
        elif contains_char(guess, word[i]) is True:
            emoji_boxes += YELLOW_BOX
        else:
            emoji_boxes += WHITE_BOX
            
        i += 1

    # Display results of user's guess.
    return emoji_boxes


def input_guess(letter_len: int) -> str:
    """Given a number, ask user for input for a blank-character word."""
    # Prompt user for a guess of appropriate length
    word: str = input(f"Enter a {letter_len} character word: ")

    while len(word) != letter_len:
        word = input(f"That wasn't {letter_len} chars! Try again: ")

    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess: str = ""
    turn_number: int = 1

    # Loop to establish user's 6 tries to guess secret word and display results.
    while turn_number < 7 and guess != secret_word:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(secret_word, guess))

        if guess == secret_word:
            print(f"You won in {turn_number}/6 turns!")

        if turn_number == 6 and guess != secret_word:
            print("X/6 - Sorry, try again tomorrow!")
        
        turn_number += 1   


# Allow python to run program as a module; allow other modules to import ex03_wordle functions.
if __name__ == "__main__":

    main()