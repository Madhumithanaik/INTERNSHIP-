import random

def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:4])

def cows_and_bulls(secret, guess):
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - cows
    return cows, bulls

def play_game():
    print("Welcome to the Cows and Bulls Game!")
    secret = generate_number()
    attempts = 0

    while True:
        guess = input("Enter a 4-digit number with non-repeating digits: ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid input. Try again.")
            continue
        attempts += 1
        cows, bulls = cows_and_bulls(secret, guess)
        print(f"{cows} cows, {bulls} bulls")
        if cows == 4:
            print(f"Congratulations! You guessed the number in {attempts} tries.")
            break

play_game()
