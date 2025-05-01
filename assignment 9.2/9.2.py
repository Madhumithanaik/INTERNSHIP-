import random

def read_words_from_file(filename):
    with open(filename, "r") as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return words

def choose_word(words):
    return random.choice(words)

def play_hangman(word_list):
    while True:
        word = choose_word(word_list)
        guessed = set()
        correct = set(word)
        tries = 6
        print("Welcome to Hangman!")

        while tries > 0:
            display_word = ' '.join([ch if ch in guessed else '_' for ch in word])
            print(display_word)
            guess = input("Guess your letter: ").upper()

            if guess in guessed:
                print("You already guessed that letter. Try again.")
                continue

            guessed.add(guess)

            if guess in correct:
                print("Correct!")
                if correct.issubset(guessed):
                    print(f"Congratulations! You guessed the word: {word}")
                    break
            else:
                tries -= 1
                print(f"Incorrect! You have {tries} chances left.")

        else:
            print(f"You lost! The word was: {word}")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            break

words = read_words_from_file("word.txt")
play_hangman(words)
