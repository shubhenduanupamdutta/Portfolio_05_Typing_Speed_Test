from tkinter import *
from random import choices
import time

# -------------------- CONSTANTS --------------------------#
WIDTH: int = 1000
HEIGHT: int = 500
FONT: tuple[str, int, str] = ("Century", 16, "normal")

with open("common_1000_words.txt", "r") as word_file:
    words = word_file.readlines()

WORDS: list[str] = [word.strip() for word in words]

# --------------------- FUNCTIONALITY ---------------------------#
start_time = None
words_to_type = choices(WORDS, k=5)
count = 0
correct_words = 0
typing_speed = 0
typing_time = 0


# def start_the_test(*args, countdown_timer=5):
#     start_test.config(text="Your test starts in:")
#
#     if countdown_timer > 0:
#         countdown.config(text=f"{countdown_timer}", background="red", foreground="white")
#         window.after(1000, start_the_test, countdown_timer - 1)
#     else:
#         typing_entry.focus()
#         countdown.config(text="", background="None")
#         global start_time
#         start_time = time.time()


# def start_timer(*args):
#     global start_time
#     start_time = time.time() + 2
#     time.sleep(2)
#     typing_entry.focus()


def update_test(*args):
    global count, correct_words, words_to_type, start_time, typing_speed, typing_time
    word_to_type = words_to_type[count]
    word_typed = typing_entry.get().split()[count].strip()
    if not start_time:
        start_time = time.time() - 1
    count += 1

    if word_typed == word_to_type:
        correct_words += 1
        current_time = time.time()
        typing_time = (current_time - start_time)
        typing_speed = int(correct_words * 60 / typing_time)
        stats.config(text=f"Typed For: {typing_time:.0f} seconds\n\n Correct Words: {correct_words}    Typing Speed: {typing_speed} WPM")

    if count == 5:
        count = 0
        typing_entry.delete(0, END)
        words_to_type = choices(WORDS, k=5)
        typing_words.config(text=f"{' '.join(words_to_type)}")


# ---------------------- USER INTERFACE -------------------------#

window = Tk()
window.title("Typing Speed Test")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=25, pady=50)

canvas = Canvas(width=(WIDTH - 10), height=150)
# canvas.config(highlightthickness=0)
logo_img = PhotoImage(file="title.png")
canvas.create_image((WIDTH - 10) / 2, 75, image=logo_img)
canvas.grid(row=0, column=0)

stats = Label(text=f"Typed For: {typing_time:.0f} seconds\n\n Correct Words: {correct_words}    Typing Speed: {typing_speed} WPM",
              font=("Century", 18, "bold"))
stats.grid(row=1, column=0, pady=20)

title_label = Label(text="Text to type:", background="lightpink", font=FONT)
title_label.grid(row=2, column=0)

typing_words = Label(text=f"{' '.join(words_to_type)}", background="white", font=("Century", 20, "normal"))
typing_words.grid(row=3, column=0, pady=10)

# start_test = Button(text="Start Test", background="lightgreen", font=FONT, command=start_timer)
# start_test.grid(row=3, column=0, pady=10)
# #
# countdown = Label(text="", font=FONT)
# countdown.grid(row=4, column=0, pady=10)


type_here = Label(text="Type Here: ", background="pink", font=FONT)
type_here.grid(row=4, column=0, pady=10)

typing_entry = Entry(background="white", width=50, takefocus=1, font=("Century", 22, "normal"))
typing_entry.focus()
typing_entry.grid(row=5, column=0, pady=10, rowspan=2)

window.bind("<space>", update_test)
window.bind("<Return>", update_test)

window.mainloop()
