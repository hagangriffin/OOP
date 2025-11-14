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
        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT,"\nElements in Stack:")
        for i in self.elements:
            txt.insert(tk.INSERT, f"\n{i}")

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, x):
        self.element.append(x)

    def dequeue(self, x):
        self.element.remove(x)

    def dis_queue(self):
        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT, self.element[0])
        for i in self.element[1:]:
            txt.insert(tk.INSERT, f"\n{i}")

queue = Queue()
stack = Stack()

top = Tk()
top.geometry("700x600")
top.title("Title")

txt = Text(top, width=60, height=15)
txt.place(x=100, y=50)

ent = Entry(top, width=60)
ent.place(x=100, y=305)



def show(x):
    if x == "enq":
        name = ent.get()
        queue.element.append(name)
        ent.delete(0, tk.END)
        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT, "\nName Queued")

    elif x == "deq":
        queue.element.pop(0)
        ent.delete(0, tk.END)
        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT, "\nName Dequeued")

    elif x == "dis":
        txt.delete("1.0", tk.END)
        queue.dis_queue()

    elif x == "s1":
        stack.push(ent.get())

    elif x == "p1":
        if len(stack.elements) > 0:
            stack.elements.pop()
        else:
            txt.delete("1.0", tk.END)
            txt.insert(tk.INSERT, "\nNo items in stack")

    elif x == "dis1":
        stack.dis()

    elif x == "adds1":
        for e in queue.element:
            stack.push(e)

        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT, "\nQueue items added to stack")

enq = Button(top, text="Enqueue", width=20, height=2, command=lambda: show("enq"))
enq.place(x=100, y=330)

deq = Button(top, text="Dequeue", width=20, height=2, command=lambda: show("deq"))
deq.place(x=100, y=380)

dis = Button(top, text="Display Queue", width=20, height=2, command=lambda: show("dis"))
dis.place(x=100, y=430)

stack1 = Button(top, text="Add to Stack", width=20, height=2, command=lambda: show("s1"))
stack1.place(x=270, y=330)

stack1_pop = Button(top, text="Pop Stack", width=20, height=2, command=lambda: show("p1"))
stack1_pop.place(x=270, y=380)

dis1 = Button(top, text="Display Stack", width=20, height=2, command=lambda: show("dis1"))
dis1.place(x=270, y=430)

add_s1 = Button(top, text="Add Queue to Stack", width=20, height=2, command=lambda: show("adds1"))
add_s1.place(x=100, y=480)

top.mainloop()