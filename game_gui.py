import tkinter as tk
import random

words = ["knife", "kid", "television", "python", "coding"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

def update_display():
    word_label.config(text=" ".join(guessed))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    guessed_label.config(text="Guessed Letters: " + " ".join(guessed_letters))

def guess_letter():
    global attempts
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1 or letter in guessed_letters:
        return

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1

    update_display()

    if "_" not in guessed:
        result_label.config(text="You won!")
        submit_btn.config(state=tk.DISABLED)
    elif attempts == 0:
        result_label.config(text=f"You lost! Word was: {word}")
        submit_btn.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Hangman Game")

word_label = tk.Label(root, text=" ".join(guessed), font=("Helvetica", 20))
word_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 16), width=5)
entry.pack()

submit_btn = tk.Button(root, text="Guess", command=guess_letter)
submit_btn.pack(pady=5)

attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Helvetica", 14))
attempts_label.pack(pady=5)

guessed_label = tk.Label(root, text="Guessed Letters: ", font=("Helvetica", 12))
guessed_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

root.mainloop()
