from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
               website: {
                       "email": email,
                       "password": password,
                 }
         }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            messagebox.showinfo(title="Alert", message="New file getting added.")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}"f"\n"f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
img_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()

email_label = Label(text="Email / Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abelkalumba@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=37)
password_entry.grid(column=1, row=3)

button_generate_password = Button(text="Generate password", highlightthickness=0, command=generate_password)
button_generate_password.grid(column=2, row=3, sticky=W)

button_add = Button(width=47, text="Add", highlightthickness=0, command=save)
button_add.grid(column=1, row=4, columnspan=2)

button_search = Button(text="Search", width=14, highlightthickness=0, command=find_password)
button_search.grid(column=2, row=1)

window.mainloop()





