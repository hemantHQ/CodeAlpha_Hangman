import random

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    print("=== Welcome to Hangman ===")
    print("Made by Hemant\n")

    words = ["knife", "kid", "television", "python", "coding"]
    word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    wrong_attempts = 0

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Wrong attempts: {wrong_attempts}/{max_attempts}")
        
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            wrong_attempts += 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You won! The word was:", word)
            break

        if wrong_attempts >= max_attempts:
            print("\n💀 You lost! The word was:", word)
            break

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == 'y':
        print("\n")
        play_hangman()
    else:
        print("Thanks for playing!")

# Start the game
play_hangman()
