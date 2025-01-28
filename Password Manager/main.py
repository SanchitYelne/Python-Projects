from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letter + password_number + password_symbol

    random.shuffle(password_letter)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the fields Empty!")
    else:
        try:
            with open(file="file_data.json", mode="r") as file_data:
                # Reading old data
                data = json.load(file_data)

        except FileNotFoundError:
            with open(file="file_data.json", mode="w") as file_data:
                json.dump(new_data, file_data, indent=4)
        else:
            # Updating old data with new
            data.update(new_data)
            with open(file="file_data.json", mode="w") as file_data:
                # Saving new data
                json.dump(new_data, file_data, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.insert(0, "sanchit@gmail.com")
            website_entry.focus()

# ---------------------------- Search --------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open(file="file_data.json", mode="r") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found")
    else:
        with open(file="file_data.json", mode="r") as file_data:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No data found for {website}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website :")
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sanchit@gmail.com")

password_label = Label(text="Password :")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=create_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)


window.mainloop()
