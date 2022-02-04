from tkinter import *

FONT = ('Arial', 20, 'normal')
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
mile_input = Entry(width=10)
mile_input.grid(column=2, row=1)

# Label Miles
mile_label = Label(text='Miles', font=FONT)
mile_label.grid(column=3, row=1)

# Label is equal to
equal_label = Label(text='is equal to', font=FONT)
equal_label.grid(column=1, row=2)
km_label = Label(text='Km', font=FONT)
km_label.grid(column=3, row=2)


def calculate():
    mile = float(mile_input.get())
    km = round(mile * 1.069344, 2)
    answer_label.config(text=f'{km}')


# Label_answer
answer_label = Label(text='', font=FONT)
answer_label.grid(column=2, row=2)

# Button
calculate_button = Button(text='Calculate', font=FONT, command=calculate)
calculate_button.grid(column=2, row=3)

window.mainloop()
