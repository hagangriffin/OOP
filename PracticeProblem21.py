import tkinter as tk
from tkinter import *

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, x):
        self.elements.append(x)

    def pop(self):
        self.elements.pop()

    def dis(self):
        txt.insert(tk.INSERT,"Elements in Stack:")
        for i in self.elements:
            txt.insert(tk.INSERT, f"\n{i}")

s1 = Stack()
s2 = Stack()

top = Tk()
top.geometry("700x500")
top.title("Stack Editor")

txt = Text(top, width=60, height=15)
txt.place(x=10, y=10)

txt.insert(tk.INSERT, """To enqueue enter the name and then click "Enqueue"\nTo dequeue click "Dequeue"\nTo display the queue click "Display Queue"\nTo add to stack enter the name and then click "Add to Stack"\nTo remove the top item from the stack """)

def show(x):
    if x == "s1":
        st1_main()
        top.withdraw()
    elif x == "s2":
        st2_main()
        top.withdraw()
    elif x == "dis1":
        txt.delete("1.0", tk.END)
        s1.dis()
    elif x == "dis2":
        txt.delete("1.0", tk.END)
        s2.dis()
    elif x == "p1":
        if len(s1.elements) > 0:
            txt.delete("1.0", tk.END)
            txt.insert(tk.INSERT, "Element Popped")
            s1.pop()
        else:
            txt.insert(tk.INSERT, "No items in stack")
    elif x == "p2":
        if len(s1.elements) > 0:
            txt.delete("1.0", tk.END)
            txt.insert(tk.INSERT, "Element Popped")
            s2.pop()
        else:
            txt.insert(tk.INSERT, "No items in stack")

stack1 = Button(top, text="Add Stack 1", width=20, height=4, command=lambda: show("s1"))
stack1.place(x=10, y=315)

stack1_pop = Button(top, text="Pop Stack 1", width=20, height=2, command=lambda: show("p1"))
stack1_pop.place(x=10, y=265)

stack2 = Button(top, text="Add Stack 2", width=20, height=4, command=lambda: show("s2"))
stack2.place(x=270, y=315)

stack2_pop = Button(top, text="Pop Stack 2", width=20, height=2, command=lambda: show("p2"))
stack2_pop.place(x=270, y=265)

dis1 = Button(top, text="Display Stack 1", width=30, height=3, command=lambda: show("dis1"))
dis1.place(x=10, y=395)

dis2 = Button(top, text="Display Stack 2", width=30, height=3, command=lambda: show("dis2"))
dis2.place(x=270, y=395)

st1 = tk.Toplevel(top)
st1.geometry("500x200")
st1.title("Stack 1")

st1_ent = Entry(st1, width=60)
st1_ent.place(x=10, y=10)

st1.withdraw()

def st1_main():
    st1.deiconify()
    def st1_show(x):
        if x == "sub":
            s1.push(st1_ent.get())
            st1_ent.delete(0, tk.END)
            top.deiconify()
            st1.withdraw()


    sub = Button(st1, text="Submit", width=15, height=1, command=lambda: st1_show("sub"))
    sub.place(x=10, y=30)

st2 = tk.Toplevel(top)
st2.geometry("500x200")
st2.title("Stack 2")

st2_ent = Entry(st2, width=60)
st2_ent.place(x=10, y=10)

st2.withdraw()

def st2_main():
    st2.deiconify()
    def st2_show(x):
        if x == "sub":
            s2.push(st2_ent.get())
            st2_ent.delete(0, tk.END)
            top.deiconify()
            st2.withdraw()

    st2_sub = Button(st2, text="Submit", width=15, height=1, command=lambda: st2_show("sub"))
    st2_sub.place(x=10, y=30)

top.mainloop()
