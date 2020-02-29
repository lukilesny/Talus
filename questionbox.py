import tkinter as tk
from tkinter import messagebox
import time


#funkcja wyswietla pytanie czy chcemy podjac cwiczenia, zwraca true/false

def questionBox():
    root = tk.Tk()
    root.withdraw()
    
    MsgBox = tk.messagebox.askquestion ('Pora sie poruszac','Hola hola! Najwyzsza pora na cwiczenia! Are you ready?',icon = 'warning')
    if MsgBox == 'yes':
        tk.messagebox.showinfo('Brawo','Zaczynamy')
        root.destroy()
        return True

    else:
        tk.messagebox.showinfo('Nie szanuje','Zastanow sie troche nad soba')
        root.destroy()
        return False

#przyklad uzycia    
time.sleep(3)
print(questionBox())
time.sleep(5)
