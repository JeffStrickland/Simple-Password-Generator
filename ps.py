# Random passowrd generator with gui

import random, string
from tkinter import *
import pyperclip

#Gui window
root = Tk()
root.geometry("400x400") 
root.title("Random Password Generator")

# Function
output_pass = StringVar()
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
def randPassGen():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)
        password = password + random.choice(char_type)
    output_pass.set(password)

# Clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())

# GUI
pass_head = Label(root, text = 'Password Length', font = 'garamond 16 bold').pack(pady= 8)
pass_label = Label(root, text = 'min 8 -  max 99 characters', font = 'garamond 10 bold').pack(pady = 5)
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 99, textvariable = pass_len, width = 5, font = 'garamond 16').pack()

# Button Generate Password
Button(root, text = "Generate Passowd" , command = randPassGen, font = "Garamond 10", bg="lightblue", fg="black", activebackground="teal", padx = 5, pady = 5).pack(pady = 20)
pass_label = Label(root, text = 'Randomly Generated Password', font = 'garamond 16 bold').pack(pady = "30 10")
Entry(root , textvariable = output_pass, width = 25, font = 'garamond 16').pack()

# Button Copy to Clipboard
Button(root, text = 'Copy to Clipboard', command = copyPass, font = 'Garamond 10', bg="lightblue", fg="black", activebackground="teal", padx=5, pady=5).pack(pady = 20)
root.mainloop()