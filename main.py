from tkinter import *

# -------------------- CONSTANTS --------------------------#
WIDTH = 800
HEIGHT = 500
FONT = ("Century", 16, "normal")

with open("common_1000_words.txt", "r") as word_file:
    words = word_file.readlines()

WORDS = [word.strip() for word in words]

# --------------------- FUNCTIONALITY ---------------------------#


# ---------------------- USER INTERFACE -------------------------#

print(WORDS)