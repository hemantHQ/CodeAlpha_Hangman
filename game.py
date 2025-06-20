import random

words = ["knife", "kid", "television", "python", "coding"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1

if "_" not in guessed:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)
