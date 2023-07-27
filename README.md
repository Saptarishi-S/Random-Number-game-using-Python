# Random-Number-game-using-Python
A number guessing game using Python and the Random module

The working of the code:
1. The `generate_number(min_val, max_val)` function:
   - This function takes two arguments, `min_val` and `max_val`, which represent the minimum and maximum values of the range within which the secret number should       be generated.
   - It uses the `random.randint()` function from the `random` module to generate a random integer within the specified range.
   - The randomly generated number is returned as the secret number.

2. The `get_hint(number, guess)` function:
   - This function takes two arguments, `number` (the secret number) and `guess` (the user's guess).
   - It provides hints to the user based on their guess in relation to the secret number.
   - If the guess is less than the secret number, it returns "The number is greater than your guess."
   - If the guess is greater than the secret number, it returns "The number is smaller than your guess."
   - If the guess is a multiple or divisible of the secret number, it returns "Your guess is a multiple or divisible of the number."
   - If none of the above conditions are met, it returns "Your guess is close, but not correct. Try again!"

3. The `main()` function:
   - This is the main function that orchestrates the entire game.
   - It starts by printing a welcome message and explaining the rules of the game.
   - It asks the user to input the minimum and maximum values for the range within which they want to guess the number.
   - It generates the secret number using the `generate_number()` function within the specified range.
   - It initializes variables to keep track of the user's score, the number of attempts made, and the user's current guess.
   - It enters a `while` loop that continues until the user guesses the correct number (i.e., when `guess` is equal to `secret_number`).
   - Inside the loop, the user is asked to input their guess, and the program provides a hint using the `get_hint()` function.
   - The user's score is reduced by 10 for each attempt using the `score -= 10` statement.
   - The loop continues until the correct number is guessed.
   - After the loop exits, the program congratulates the user for guessing the number correctly and displays the number of attempts made and the final score.

4. The `if __name__ == "__main__":` block:
   - This block ensures that the `main()` function is only called if the script is run directly (not imported as a module into another script).
   - When the script is run, the `main()` function is called, and the game starts.

To play the game, the user is prompted to enter the range for the number they want to guess (e.g., 1 to 10 or 1 to 100). The program then randomly selects a secret number within that range. The user continues to guess the number until they get it right. For each incorrect guess, the user receives a hint, and their score is reduced. The game ends with a congratulations message, displaying the number of attempts made and the final score.
