from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=1)
email_label = Label(text="Email/Username:")
email_label.grid(row=2)
password_label = Label(text="password:")
password_label.grid(row=3)

# Entries
website_label = Entry(width=35)
website_label.grid(row=1, column=1, columnspan=2)
email_label = Entry(width=35)
email_label.grid(row=2, column=1, columnspan=2)
password_label = Entry(width=21)
password_label.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=4, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
