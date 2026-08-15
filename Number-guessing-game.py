import random

HIGH_SCORE_FILE = "Hi-score.txt"


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            content = file.read().strip()
            return int(content) if content else None
    except (FileNotFoundError, ValueError):
        return None


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


def get_guess():
    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            if 1 <= guess <= 100:
                return guess
            print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def show_feedback(guesses):
    if guesses <= 10:
        print("Incredible! You guessed it in very few attempts.")
    elif guesses < 20:
        print("Good work. Try to improve the attempt count next time.")
    else:
        print("That took many attempts. Keep practicing.")


def main():
    secret_number = random.randint(1, 100)
    guesses = 0
    high_score = load_high_score()

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        guesses += 1
        guess = get_guess()

        if guess == secret_number:
            print(f"You guessed the correct number in {guesses} attempts.")
            break
        if guess < secret_number:
            print("Higher number, please.")
        else:
            print("Lower number, please.")

    show_feedback(guesses)

    if high_score is None:
        save_high_score(guesses)
        print(f"First high score saved: {guesses}")
    elif guesses < high_score:
        save_high_score(guesses)
        print(f"New high score: {guesses}")
    elif guesses == high_score:
        print(f"You matched the high score: {high_score}")
    else:
        print(f"Current high score is {high_score}. Try to beat it next time.")


if __name__ == "__main__":
    main()
