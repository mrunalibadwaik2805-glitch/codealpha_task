# Hangman Game

import random

# List of predefined words
words = ["python", "laptop", "network", "college", "keyboard"]

# Select a random word
word = random.choice(words)

# Create hidden word using underscores
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong Guesses Left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")

# Result
if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n❌ Game Over!")
    print("The correct word was:", word)







