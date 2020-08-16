import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import random
Target = random.randint(0,9)
Count = 0
root = tk.Tk()
root.withdraw()

while Count < 3:
    usr_input = simpledialog.askinteger(title="Input", prompt="Guess a Number from (0,9):")
    if usr_input == Target:
        messagebox.showinfo(title="ALERT",message="You won the game")
        exit()
    else:
        if Count < 2:
            messagebox.showinfo(title = "ALERT",message=  'Mismatch! Try again')
        else:
            messagebox.showinfo(title = 'ALERT',message = f'GAME ENDED \n ANSWER is {Target}')
    Count += 1





