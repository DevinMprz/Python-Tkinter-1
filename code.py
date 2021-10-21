from tkinter import *
from tkinter.ttk import Combobox
from typing import Collection
def clicked():##функція при натисканні на кнопку результату
    if move.get() == "+":##додавання
        res = int(firstNum.get()) + int(secNum.get())
        print(firstNum, " ", secNum, " ", res)
        lbl.configure(text=res)
    elif move.get() == "-":##віднімання
        res = int(firstNum.get()) - int(secNum.get())
        print(firstNum, " ", secNum, " ", res)
        lbl.configure(text=res)
    elif move.get() == "*":##множення
        res = int(firstNum.get()) * int(secNum.get())
        print(firstNum, " ", secNum, " ", res)
        lbl.configure(text=res)
    elif move.get() == "/":##ділення
        res = float(firstNum.get()) / float(secNum.get())
        print(firstNum, " ", secNum, " ", res)
        lbl.configure(text=res)
    elif move.get() == "**":##піднесення до степіню
        res = int(firstNum.get()) ** int(secNum.get())
        print(firstNum, " ", secNum, " ", res)
        lbl.configure(text=res)
    else:
        lbl.configure(text="Error", font="bold",background="red")##виведення помилки
def DarkTheme():
    firstNum.configure(background="black", foreground="#FFFFFF")
    secNum.configure(background="black", foreground="#FFFFFF")
    move.configure(background="black", foreground="#FFFFFF")
    lbl.configure(foreground="white")
    rad1.configure(background="black", foreground="#FFFFFF")
    rad2.configure(background="black", foreground="#FFFFFF")
    window.configure(background="#363636")
def LightTheme():
    firstNum.configure(background="white", foreground="black")
    secNum.configure(background="white", foreground="black")
    move.configure(background="white", foreground="black")
    lbl.configure(foreground="black")
    rad1.configure(background="#d6d6d6",foreground="black")
    rad2.configure(background="#d6d6d6",foreground="black")
    window.configure(background="#d6d6d6")
window = Tk()##створення вікна
window.title("code.py")##Назва вікна
window.geometry('400x250')##Розміри вікна
lbl = Label(window, text="0")##рядок Результату
lbl.grid(column=4, row=0)##положення рядку Результату
firstNum = Entry(window,width=5, justify='center')##рядок першого числа
firstNum.grid(column=0, row=0)##положення рядку першого числа
move = Combobox(window, width=3, justify='center')##рядок дії
move['values'] = ("+", "-", "*", "/", "**")
move.grid(column=1, row=0)##положення рядку дії
secNum = Entry(window,width=5, justify='center')##рядок другого числа
secNum.grid(column=2, row=0)##положення рядку другого числа
btn = Button(window, text="=", width=2, command=clicked)##кнопка результату
btn.grid(column=3, row=0)##положення кнопки результату
rad1 = Radiobutton(window, text='Dark', value=1, command=DarkTheme)
rad2 = Radiobutton(window, text='Light', value=2, command=LightTheme)
rad1.grid(column=10, row=0)
rad2.grid(column=10, row=2)
window.mainloop()