import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD SEARCHER ------------------------------- #
def searcher():
    target_site = site_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            # reading old data
            data = json.load(data_file)  # 讀取
    except FileNotFoundError:
        messagebox.showwarning(title='error', message='No Data File Found')
    else:
        if target_site in data:
            target_email = data[target_site]['email']
            target_password = data[target_site]['password']
            messagebox.showinfo(title=target_site, message=f'Email:{target_email}\nPassword:{target_password}')
        else:
            messagebox.showwarning(title='Error', message=f'No Data for {target_site} Found.')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    char_letters = [random.choice(letters) for _ in range(nr_letters)]
    char_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    char_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = char_letters + char_symbols + char_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        site: {
            'email': email,
            'password': password
        }

    }

    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message="Please don't leave any fields empty!")

    else:
        try:
            with open('data.json', 'r') as data_file:
                # reading old data
                data = json.load(data_file)  # 讀取
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update
            data.update(new_data)
            # saving the new data
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)  # 寫入
        finally:
            site_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label & entry
site_label = Label(text='Website:   ')
site_label.grid(column=0, row=1)
site_entry = Entry(width=21)
site_entry.grid(column=1, row=1)
site_entry.focus()  # focus the cursor in the entrybox

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'mushroomzly@gmail.com')

pass_label = Label(text='Password:   ')
pass_label.grid(column=0, row=3)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Button
generate_button = Button(text='Generate Password', command=generator)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='search', width=13, command=searcher)
search_button.grid(column=2, row=1)
window.mainloop()
