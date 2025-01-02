import random

# Prompt the user for their name
print("Hi, Enter your name:-")
name = input("enter your name:-")

# List of fruits to choose from
fruit_list = ["apple", "mango", "grapes", "orange", "pineapple"]

# Randomly choose a fruit
fruit = random.choice(fruit_list)

user_guess = ""
guesses = 6  # Number of guesses

# Main game loop
while guesses > 0:
    # Prompt for the user's character guess
    char = input("Guess a character: ").lower()

    # Check if the character has already been guessed
    if char in user_guess:
        print(f"You have already guessed this character: {char}")
        continue  # Skip the rest of the loop if the letter is already guessed
    
    user_guess += char  # Add the guessed character to the user guesses

    # Check if the guessed character is in the fruit
    if char in fruit:
        print(f"You've guessed correctly: {char}")
    else:
        guesses -= 1  # Decrease the guesses if incorrect
        print(f"You have {guesses} guesses left.")

    # Display the word with underscores for unguessed letters
    display_word = ""
    for letter in fruit:
        if letter in user_guess:
            display_word += letter  # Show the correct letter
        else:
            display_word += "_"  # Show an underscore for unguessed letters

    print("Word so far:", display_word)

    # Check if the player has guessed the whole word
    if "_" not in display_word:
        print(f"Congratulations! You guessed the word: {fruit}")
        break  # End the game if the word is guessed

# If the player runs out of guesses
if guesses == 0:
    print(f"You lost! The correct word was: {fruit}")
