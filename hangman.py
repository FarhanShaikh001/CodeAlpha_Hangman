import random

# List of words
words = ["python", "coding", "laptop", "mobile", "apple"]

# Select random word
word = random.choice(words)

# Store guessed letters
guessed = []

print("Welcome to Hangman!")
print("Guess the word")

while True:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You won 🎉")
        break

    guess = input("Enter a letter: ").lower()

    if guess not in guessed:
        guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
