#Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(ch if ch in guesses else "_" for ch in secret_word)
        print(display)
        return "_" not in display

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").strip().lower()
    game = make_hangman(secret_word)

    done = False
    while not done:
        letter = input("Guess a letter: ").strip().lower()
        done = game(letter)

    print("You guessed the word!")
