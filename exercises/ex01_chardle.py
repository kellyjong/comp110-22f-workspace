"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730477669"

word: str = input("Enter a 5-character word: ")
length_word: int = len(word)
if length_word != 5:
    print("Error: Word must contain 5 characters")
    exit()

guess: str = input("Enter a single character: ")
length_guess: int = len(guess)
if length_guess != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + guess + " in " + word)

i: int = 0
count: int = 0
if word[i] == guess:
    print(guess + " found at index " + str(i))
    count = count + 1

i = i + 1
if word[i] == guess:
    print(guess + " found at index " + str(i))
    count = count + 1

i = i + 1
if word[i] == guess:
    print(guess + " found at index " + str(i))
    count = count + 1

i = i + 1
if word[i] == guess:
    print(guess + " found at index " + str(i))
    count = count + 1

i = i + 1
if word[i] == guess:
    print(guess + " found at index " + str(i))
    count = count + 1

if count == 0:
    print("No instances of " + guess + " found in " + word)

if count == 1:
    print("1 instance of " + guess + " found in " + word)

if count > 1:
    print(str(count) + " instances of " + str(guess) + " found in " + word)