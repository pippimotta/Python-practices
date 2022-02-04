import tkinter

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20,pady=10)
#Label
my_label = tkinter.Label(text='I am a label', font=('Arial', 20, 'normal'))
# my_label.pack() # display the label in certain position
my_label['text'] = 'New text'
my_label.config(text='New text')
# 用padx/pady add space
my_label.config(padx=20, pady=10)
my_label.grid(column=1, row=1)#grid用相對位置決定座標
#相對於turtle來說，tkinter.label()的參數傳入比較無限
#advanced Python Arguments
# def(*args) --* accepet any number of arguments

# Button
def button_cliked():
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text='Click Me', command= button_cliked)
# button.pack()
button.grid(column=2, row=2)

new_button = tkinter.Button(text='New Button')
new_button.grid(column=3, row=1)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=4,row=3)

window.mainloop() # keep the window displayed

print(1%2)