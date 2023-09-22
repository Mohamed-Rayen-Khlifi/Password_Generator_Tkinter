from random import randint
import tkinter as tk

root = tk.Tk()

root.geometry("750x500")
root.title("Password Generator")

label = tk.Label(root, text="Password Generator", font=("Arial", 18)).pack(
    padx=20, pady=20
)

textbox = tk.Text(root, height=3, font=("Arial", 18)).pack(padx=10)


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

symbols = ''


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
    print(symbols)

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
)

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

button = tk.Button(root, text="Generate Password", font=("Arial, 18"), command=generate_password).pack(pady=10)

root.mainloop()







# length = int(input("6] Please provide the length of your password: "))

# symbols = ""

# if numbers_prompt == "y":
# symbols += numbers
# if characters_prompt == "y":
# symbols += characters
# if special_characters_prompt == "y":
# symbols += special_characters
# if majus_characters_prompt == "y":
# symbols += majus_charaters

# if symbols == "":
# print("Empty password!")
# else:
# response = ""
# while response != "q":
# password = ""
# if first_name == "y":
# password += first_three[0:3]
# i = 0
# while i < length:
# password += symbols[randint(0, len(symbols) - 1)]
# i += 1
# print("Your password is ---------->","\033[1m","\033[93m",password,"\033[0m","<----------",)
# response = input("Continue? (Enter/q): ")
