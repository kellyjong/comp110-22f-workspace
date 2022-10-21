"""EX06 - Choose Your Own Adventure: Number Guessing."""

__author__ = "730477669."

from random import randint

EXCLAMATION_POINT: str = "\U00002763"
EMOJI_FACE: str = "\U0001F636"
EMOJI_SMILE: str = "\U0001F606"

# Points represents the number of attempts it takes the user to guess the number correctly
points: int 
player: str 
rand_number: int
upper_bound: int


def main() -> None:
    """Main procedure that allows for the program to run."""
    global points, player, upper_bound
    points = 0
    player = ""
    upper_bound = 10

    option: int = 0

    greet()

    while option != 3:
        print(f"\nYou are currently at {points} attempts.")
        option = int(input("Enter a number: \n1. Continue playing this game guessing a number 0-10. \n2. Change the upper value of the range of numbers to guess. \n3. Exit the game\n"))
    
        if option == 1:
            user_guess()

        elif option == 2:
            upper_bound = int(input(f"{player}, what do you want the new upper bound to be? If the upper bound is lower than {upper_bound}, each try will count as 2 attempts. "))
            
            if upper_bound < 10:
                points = lower_upper(upper_bound, points)
                
            else:
                user_guess()

    if option == 3:
        print(f"Goodbye {player}! You ended at {points} attempts. {EMOJI_SMILE}")
        quit()


def greet() -> None:
    """Prints welcome message, gets user's name, and explains the rules of the game."""
    print(f"Welcome to Guess a Number {EXCLAMATION_POINT}")

    global player
    player = input("What's your name? ")

    print("A number from 0-10 will be randomly generated. If your guess matches with this number, you win a point!")


def user_guess() -> None:
    """Obtains guess from user and checks whether guess is the same as the random number."""
    global points, player, rand_number
    rand_number = randint(0, 10)
    specific_points: int = 0

    guess = int(input(f"Hi, {player}. What is your guess? "))
    points += 1
    specific_points += 1

    if guess == rand_number:
        print(f"Good Job {player}! You guessed the number in {specific_points} attempts {EMOJI_SMILE}!")

    else:
        while guess != rand_number:
            guess = int(input(f"That's not the number.{EMOJI_FACE}. Try again! "))
            points += 1
            specific_points += 1

        print(f"Good Job {player}! You guessed the number in {specific_points} attempts {EMOJI_SMILE}!")


def lower_upper(upper_bound: int, initial_points: int) -> int:
    """Changes the upper bound to a number the user inputs that is less than 10. Increments the points variable accordingly."""
    global player, rand_number
    specific_points: int = 0

    rand_number = randint(0, upper_bound)

    guess = int(input(f"Hi, {player}. What is your guess? "))
    initial_points += 2
    specific_points += 2

    if guess == rand_number:
        print(f"Good Job {player}! You guessed the number in {specific_points} attempts {EMOJI_SMILE}!")

    else:
        while guess != rand_number:
            guess = int(input(f"That's not the number.{EMOJI_FACE}. Try again! "))
            initial_points += 2
            specific_points += 2
        
        print(f"Good Job {player}! You guessed the number in {specific_points} attempts {EMOJI_SMILE}!")
            
    return initial_points


if __name__ == "__main__":
    main()