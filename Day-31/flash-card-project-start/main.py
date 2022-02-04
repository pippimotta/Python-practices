BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ('Arial', 40, 'italic')
TEXT_FONT = ('Arial', 60, 'bold')
from tkinter import *
import pandas
import random

current_card = {}
learn_card = []
# ----------------------------CREATE NEW FLASH CARDS------------------------------- #
# read data from csv
try:
    data = pandas.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


# define command
def show_new_card():
    global current_card

    current_card = random.choice(word_list)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(text_text, text=current_card['French'], fill='black')
    window.after(3000, flip)

# ----------------------------UPDATE CARD------------------------------ #
def is_known():
    word_list.remove(current_card)
    new_data = pandas.DataFrame(word_list)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    learn_card.append(current_card)
    review = pandas.DataFrame(learn_card)
    review.to_csv('data/review.csv', index=False)
    show_new_card()

# ---------------------------- CARD FLIP ------------------------------- #
def flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(text_text, text=current_card['English'], fill='white')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text='French', font=TITLE_FONT)


text_text = canvas.create_text(400, 263, font=TEXT_FONT)

known_img = PhotoImage(file='images/right.png')
known_button = Button(image=known_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)
unknown_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=unknown_img, highlightthickness=0, command=show_new_card)
unknown_button.grid(column=0, row=1)

show_new_card()

window.mainloop()
