import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x600")

answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        elif x == "C":
            answer.delete(1.0, END)

        elif x == "<-":
            answer.delete("insert-1c", "insert")

        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)


b1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
b1.place(x=100, y=150)
b2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
b2.place(x=175, y=150)
b3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
b3.place(x=250, y=150)
b4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
b4.place(x=100, y=225)
b5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
b5.place(x=175, y=225)
b6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
b6.place(x=250, y=225)
b7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
b7.place(x=100, y=300)
b8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
b8.place(x=175, y=300)
b9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
b9.place(x=250, y=300)
plus = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
plus.place(x=100, y=375)
minus = Button(top, text="-", width=10, height=5, command=lambda: show("-"))
minus.place(x=100, y=450)
b0 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))
b0.place(x=175, y=375)
times = Button(top, text="*", width=10, height=5, command=lambda: show("*"))
times.place(x=250, y=375)
eq = Button(top, text="=", width=10, height=5, command=lambda: show("="))
eq.place(x=175, y=450)
div = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
div.place(x=250, y=450)

clear = Button(top, text="C", width=10, height=5, command=lambda: show("C"))
clear.place(x=325, y=150)

back = Button(top, text="<-", width=10, height=5, command=lambda: show("<-"))
back.place(x=325,y=225)



top.mainloop()

