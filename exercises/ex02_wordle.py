"""Making a wordle"""

__author__: str = "730661635"


def contains_char(word: str, letter: str) -> bool:
    """Checks if the letter is anywhere in the word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    i = 0
    while i < len(
        word
    ):  # Checks to see if a certain letter is in the word at any index"
        if word[i] == letter:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Makes the emoji boxes for each letter"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    emojified_result = ""
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:  # Green box if correct letter in correct spot
            emojified_result += GREEN_BOX
        elif contains_char(
            word=secret, letter=guess[i]
        ):  # Yellow box if correct letter in wrong spot"
            emojified_result += YELLOW_BOX
        else:  # White box if incorrect letter
            emojified_result += WHITE_BOX
        i += 1  # Checks every letter in the word
    return emojified_result


def input_guess(char: int) -> str:
    """Checks if the guess is the correct number of letters"""
    guess = input(f"Enter a {char} character word:")
    while (
        len(guess) != char
    ):  # Makes sure guess is the same number of letters as the correct word"
        guess = input(f"That wasn't {char} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    won = False
    while turns <= 6 and not won:
        print(f"===Turn {turns}/6 ===")
        returned_value = input_guess(char=len(secret))
        print(emojified(guess=returned_value, secret=secret))
        if returned_value == secret:
            won = True
        else:
            turns += 1
    if won:
        print(f"You won in {turns}/6 turns!")
    if turns > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
