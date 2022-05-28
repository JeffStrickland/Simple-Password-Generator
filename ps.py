# Random password generator 
# GUI with tkinter
# Python 3

import random, string
from tkinter import *
import tkinter as tk
import pyperclip

#Gui window configuration
root = Tk()
root.geometry("400x400") 
root.title("Random Password Generator")
root.configure(background="lightgray")

# Password Variables from checkboxes
output_pass = StringVar()
upper = tk.IntVar()
lower = tk.IntVar()
digits = tk.IntVar()
sc = tk.IntVar()

# Password Variables Function
def char_type():
    combi = []
    if upper.get() == 1:
        combi.append(string.ascii_uppercase)
    else:
        pass
    if lower.get() == 1:
        combi.append(string.ascii_lowercase)
    else:
        pass
    if digits.get() == 1:
        combi.append(string.digits)
    else:
        pass
    if sc.get() == 1:
        combi.append(string.punctuation)
    else:
        pass 
    return combi 

# Password Generator Function
def randPassGen():
    password = ""
    for y in range(pass_len.get()):
        char_selection = random.choice(char_type())
        password = password + random.choice(char_selection)
    output_pass.set(password)

# Clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())

# GUI Component Layout Top
pass_head = Label(root, text = 'Password Options', font = 'garamond 14 bold', bg='lightgray').pack(pady=20)
pass_label = Label(root, text = 'Length min 8 -  max 99', font = 'garamond 12 bold', bg='lightgray').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 99, textvariable = pass_len, width = 5, font = 'garamond 16').pack(pady=10)

# Checkboxes Middle
c = Checkbutton(root, variable=upper, onvalue=1, offvalue=0, text = "Uppercase", font = "Garamond 12 bold", bg = 'lightgray', fg = "black", activebackground = 'teal', width=20).pack(anchor=CENTER)
c1 = Checkbutton(root, variable=lower, onvalue=1, offvalue=0, text = "Lowercase", font = "Garamond 12 bold", bg = 'lightgray', fg = "black", activebackground = 'teal', width=20).pack(anchor=CENTER)
c2 = Checkbutton(root, variable=digits, onvalue=1, offvalue=0, text = "Numbers", font = "Garamond 12 bold", bg = 'lightgray', fg = "black", activebackground = 'teal', width=20).pack(anchor=CENTER)
c3 = Checkbutton(root, variable=sc, onvalue=1, offvalue=0, text = "Special Characters", font = "Garamond 12 bold", bg = 'lightgray', fg = "black", activebackground = 'teal', width=20).pack(anchor=CENTER)

# Button Generate Password Bottom
Button(root, text = "Generate Password" , command = randPassGen, font = "Garamond 14", bg = "lightblue", fg="black", activebackground="teal").pack(pady=10)
pass_label = Label(root, text = 'Randomly Generated Password', font = 'garamond 14 bold', bg='lightgray').pack(pady=20)

# Password Output
Entry(root , textvariable = output_pass, width = 25, font = 'garamond 16').pack()

# Button Copy to Clipboard
Button(root, text = 'Copy to Clipboard', command = copyPass, font = 'Garamond 12', bg="lightblue", fg="black", activebackground="teal", padx=5, pady=5).pack(pady =5)

root.mainloop()