import random

# Initializing game
print("Hi, Please enter your name:")
name = input("Enter your name: ")
print(f"Good luck, {name}!\n")

# List of words to choose from
word_list = ["apple", "mango", "grapes"]
random_word = random.choice(word_list)

# Game variables
guesses = ""  # Store the letters guessed by the user
turns = 12  # Number of turns the player gets

# Main game loop
while turns > 0:
    failed = 0  # Reset failed count for each turn

    # Display the word with blanks for unguessed characters
    print("\nWord: ", end="")
    for char in random_word:
        if char in guesses:
            print(char, end=" ")  # If guessed, print the character
        else:
            print('_', end=" ")  # If not guessed, print '_'
            failed += 1  # Increment failed counter if the letter isn't guessed

    print()  # Newline after word display for better readability

    # Check if the player has guessed all the characters correctly
    if failed == 0:
        print(f"\nCongratulations, {name}! You win!")
        print(f"The word is: {random_word}")
        break  # Exit the game if the player wins

    # Ask the player to guess a character
    no_of_guess = input("Guess a character: ").lower()

    # Add the guessed character to the list of guesses
    if no_of_guess not in guesses:
        guesses += no_of_guess
    else:
        print("You've already guessed that letter.")

    # Check if the guess is correct or not
    if no_of_guess not in random_word:
        turns -= 1  # Decrease the number of turns for incorrect guesses
        print("Wrong guess!")
        print(f"You have {turns} more guesses left.")
    else:
        print("Good guess!")

    # If the player runs out of turns, they lose
    if turns == 0:
        print(f"\nSorry, {name}. You lose!")
        print(f"The correct word was: {random_word}")
