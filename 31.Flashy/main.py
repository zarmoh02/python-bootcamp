from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
# reading through csv file
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/italian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="Italian", fill="black")
    canvas.itemconfig(word_text, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)


def flip_card(_):
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 264, image=card_front_img)
title_text = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 250, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

check_button_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_img, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=0)

cross_button_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_button_img, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=1)

# flip the card by clicking
canvas.bind("<Button-1>", flip_card)

next_card()

window.mainloop()
