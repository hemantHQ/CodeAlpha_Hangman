import tkinter as tk
import random

def start_game():
    global word, guessed, attempts, guessed_letters
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    for btn in alphabet_buttons:
        btn.config(state=tk.NORMAL, bg="lightgray", text=btn["text"].strip(" ❌"))
    hint_btn.config(state=tk.NORMAL)
    result_overlay.place_forget()
    update_display()
    draw_hangman(0)
    show_frame(game_frame)

def update_display():
    word_label.config(text=" ".join(guessed))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    draw_hangman(6 - attempts)

def guess_letter(letter, btn=None):
    global attempts
    letter = letter.lower()
    if letter in guessed_letters or not letter.isalpha():
        return

    guessed_letters.append(letter)

    if btn:
        btn.config(state=tk.DISABLED)
    else:
        for b in alphabet_buttons:
            if b["text"].lower() == letter:
                b.config(state=tk.DISABLED)

    if letter in word:
        if btn: btn.config(bg="lightgreen")
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        if btn: btn.config(bg="red", text=f"{letter.upper()} ❌")

    update_display()

    if "_" not in guessed:
        show_result("🎉 You won!")
    elif attempts == 0:
        show_result(f"💀 You lost! Word was: {word}")

def give_hint():
    for i in range(len(word)):
        if guessed[i] == "_":
            guessed[i] = word[i]
            update_display()
            for btn in alphabet_buttons:
                if btn["text"].lower() == word[i]:
                    btn.config(state=tk.DISABLED, bg="yellow")
            if "_" not in guessed:
                show_result("🎉 You won!")
            return

def disable_all_buttons():
    for btn in alphabet_buttons:
        btn.config(state=tk.DISABLED)
    hint_btn.config(state=tk.DISABLED)

def show_result(message):
    disable_all_buttons()
    result_message.config(text=message)
    result_overlay.place(relx=0.5, rely=0.5, anchor="center")

def draw_hangman(stage):
    canvas.delete("all")
    canvas.create_line(20, 280, 180, 280)
    canvas.create_line(70, 280, 70, 20)
    canvas.create_line(70, 20, 150, 20)
    canvas.create_line(150, 20, 150, 50)

    if stage >= 1:
        canvas.create_oval(130, 50, 170, 90)
    if stage >= 2:
        canvas.create_line(150, 90, 150, 150)
    if stage >= 3:
        canvas.create_line(150, 100, 120, 130)
    if stage >= 4:
        canvas.create_line(150, 100, 180, 130)
    if stage >= 5:
        canvas.create_line(150, 150, 120, 200)
    if stage >= 6:
        canvas.create_line(150, 150, 180, 200)

def show_frame(frame):
    frame.tkraise()

def on_key_press(event):
    if game_frame.winfo_ismapped():
        letter = event.char.lower()
        for btn in alphabet_buttons:
            if btn["text"].lower() == letter and btn["state"] == tk.NORMAL:
                guess_letter(letter, btn)
                break

# --------------------------- GUI SETUP ---------------------------

root = tk.Tk()
root.title("Hangman Game")
root.state("zoomed")  # Maximize the window (not fullscreen)
root.configure(bg="#f0f0f0")
root.bind("<Key>", on_key_press)

# Frames
main_frame = tk.Frame(root, bg="#f0f0f0")
game_frame = tk.Frame(root, bg="#f0f0f0")

for frame in (main_frame, game_frame):
    frame.place(relwidth=1, relheight=1)

# --------------------------- MAIN MENU ---------------------------

main_title = tk.Label(main_frame, text="HANGMAN", font=("Helvetica", 64, "bold"), bg="#f0f0f0")
main_title.pack(pady=150)

start_button = tk.Button(main_frame, text="▶ New Game", font=("Helvetica", 28), command=start_game, bg="#4CAF50", fg="white", width=20)
start_button.pack(pady=20)

exit_button = tk.Button(main_frame, text="❌ Exit", font=("Helvetica", 24), command=root.quit, bg="#d9534f", fg="white", width=20)
exit_button.pack(pady=10)

footer_main = tk.Label(main_frame, text="Made by Hemant", font=("Helvetica", 14), bg="#f0f0f0", fg="gray")
footer_main.pack(side=tk.BOTTOM, pady=10)

# --------------------------- GAME UI ---------------------------

word_label = tk.Label(game_frame, text="", font=("Helvetica", 48), bg="#f0f0f0")
word_label.pack(pady=30)

attempts_label = tk.Label(game_frame, text="", font=("Helvetica", 24), bg="#f0f0f0")
attempts_label.pack()

canvas = tk.Canvas(game_frame, width=300, height=300, bg="white", highlightthickness=2, highlightbackground="black")
canvas.pack(pady=20)

keyboard_frame = tk.Frame(game_frame, bg="#f0f0f0")
keyboard_frame.pack(pady=10)

alphabet_buttons = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
row1, row2 = alphabet[:13], alphabet[13:]

for row_letters in [row1, row2]:
    row_frame = tk.Frame(keyboard_frame, bg="#f0f0f0")
    row_frame.pack()
    for letter in row_letters:
        btn = tk.Button(row_frame, text=letter, width=5, height=2, font=("Helvetica", 18), bg="lightgray")
        alphabet_buttons.append(btn)

for btn in alphabet_buttons:
    btn.config(command=lambda b=btn: guess_letter(b["text"].lower(), b))
    btn.pack(side=tk.LEFT, padx=2, pady=4)

hint_btn = tk.Button(game_frame, text="💡 Hint", font=("Helvetica", 18), command=give_hint, bg="#ffe680")
hint_btn.pack(pady=15)

result_overlay = tk.Frame(game_frame, bg="black")
result_overlay.configure(width=600, height=250)
result_overlay.place_forget()
result_overlay.place(relx=0.5, rely=0.5, anchor="center")
result_overlay.pack_propagate(False)

result_message = tk.Label(result_overlay, text="", font=("Helvetica", 36), fg="white", bg="black")
result_message.pack(pady=30)

play_again_btn = tk.Button(result_overlay, text="🔁 Play Again", font=("Helvetica", 20), command=start_game, bg="white")
play_again_btn.pack()

footer_game = tk.Label(game_frame, text="Made by Hemant", font=("Helvetica", 14), bg="#f0f0f0", fg="gray")
footer_game.pack(side=tk.BOTTOM, pady=10)

# --------------------------- GAME STARTUP ---------------------------
words = ["python", "intern", "hangman", "project", "coding"]
word = ""
guessed = []
guessed_letters = []
attempts = 6

show_frame(main_frame)
root.mainloop()
