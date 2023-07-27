import random

def generate_number(min_val, max_val):
    return random.randint(min_val, max_val)

def get_hint(number, guess):
    if guess < number:
        return "The number is greater than your guess."
    elif guess > number:
        return "The number is smaller than your guess."
    elif guess % number == 0 or number % guess == 0:
        return "Your guess is a multiple or divisible of the number."
    else:
        return "Your guess is close, but not correct. Try again!"

def main():
    print("Welcome to the Number Guessing Game!")
    print("You will be given a range, and you have to guess the number within that range.")
    print("Each time you make a wrong guess, your score will be reduced.\n")

    min_val = int(input("Enter the minimum value of the range: "))
    max_val = int(input("Enter the maximum value of the range: "))
    secret_number = generate_number(min_val, max_val)

    score = 100
    attempts = 0
    guess = 0

    while guess != secret_number:
        guess = int(input("Guess the number: "))
        attempts += 1
        hint = get_hint(secret_number, guess)
        print(hint)
        score -= 10  # Reducing score for every attempt

    print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts.")
    print(f"Your final score is: {score}")

if __name__ == "__main__":
    main()
