from random import randint
import tkinter as tk


root = tk.Tk()


padding_x = 20
padding_y = 20

fg_color = "#12F5F9"
bg_color = "white"

numbers = tk.BooleanVar()
low_case = tk.BooleanVar()
capital_case = tk.BooleanVar()
special_char = tk.BooleanVar()
f_name = tk.BooleanVar()

numbers = "0123456789"
lower_case_characters = "abcdefghijklmnopqrstuvwxyz"
capital_case_charaters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = '²&é"()-è_çà)=^$*ù!:;,<>/%§/.?°@'

symbols = ""


def add_numbers():
    global symbols
    symbols += numbers


def add_lower():
    global symbols
    symbols += lower_case_characters


def add_capital():
    global symbols
    symbols += capital_case_charaters


def add_special():
    global symbols
    symbols += special_characters


def generate_password():
    global symbols
    global length
    password = ""
    loop_num = length.get("1.0", "end-1c")
    if symbols == "":
        password = "Empty password"
    else:
        i = 0
        while i < int(loop_num):
            password += symbols[randint(0, len(symbols) - 1)]
            i += 1
        passwd = tk.Text(root, font=("Arial, 18"), height=1, width=25)

        passwd.insert("1.0", password)
        passwd.pack(padx=padding_x, pady=padding_y)


root.geometry("1500x1500")
root.title("Password Generator")

label = tk.Label(root, text="Password Generator", font=("Arial", 18)).pack(
    padx=padding_x, pady=padding_y
)

numbers_check = tk.Checkbutton(
    root,
    text="Numbers",
    variable=numbers,
    onvalue=True,
    offvalue=False,
    command=add_numbers,
    font=("Arial", 18),
    fg=fg_color,
    bg=bg_color,
    padx=padding_x,
    pady=padding_y,
    compound="left",
).pack()

lower_case_char_check = tk.Checkbutton(
    root,
    text="Lower case characters",
    variable=low_case,
    onvalue=True,
    offvalue=False,
    command=add_lower,
    font=("Arial", 18),
    fg=fg_color,
    bg=bg_color,
    padx=padding_x,
    pady=padding_y,
    compound="left",
).pack()

capital_case_char_check = tk.Checkbutton(
    root,
    text="Capital case characters",
    variable=capital_case,
    onvalue=True,
    offvalue=False,
    command=add_capital,
    font=("Arial", 18),
    fg=fg_color,
    bg=bg_color,
    padx=padding_x,
    pady=padding_y,
    compound="left",
).pack()

special_char_check = tk.Checkbutton(
    root,
    text="Special characters",
    variable=special_char,
    onvalue=True,
    offvalue=False,
    command=add_special,
    font=("Arial", 18),
    fg=fg_color,
    bg=bg_color,
    padx=padding_x,
    pady=padding_y,
    compound="left",
).pack()

length = tk.Text(root, font=("Arial", 18), height=4, width=25)
length.insert("1.0", "Please specify the length of your password")
length.pack(padx=padding_x, pady=padding_y)


button = tk.Button(
    root, text="Generate Password", font=("Arial, 18"), command=generate_password
).pack(pady=10)

root.mainloop()
