from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_numbers + pass_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='OOPS', message='Fill the blank fields')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_pass():
    website = website_input.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='ERROR', message='No Data Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='ERROR', message=f'No details for {website} exists.')

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Labels
text_website = Label(text='Website:', font=('Arial', 12, 'italic'))
text_website.grid(column=0, row=1)
text_website.config(padx=10, pady=10)

email_text = Label(text='Email/Username:', font=('Arial', 12, 'italic'))
email_text.grid(column=0, row=2)
email_text.config(padx=10, pady=10)

pass_text = Label(text='Password:', font=('Arial', 12, 'italic'))
pass_text.grid(column=0, row=3)
pass_text.config(padx=10, pady=10)

# Buttons
gen_button = Button(text='Generate Password', command=pass_generate)
gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=40, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=15, command=find_pass)
search_button.grid(column=2, row=1)

# Entries
email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'example@gmail.com')

website_input = Entry(width=25)
website_input.grid(column=1, row=1)
website_input.focus()

pass_input = Entry(width=25)
pass_input.grid(column=1, row=3)

window.mainloop()

