import tkinter as tk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, x):
        self.element.append(x)

    def dequeue(self, x):
        self.element.remove(x)

    def dis_queue(self):
        txt.insert(tk.INSERT, self.element[0])
        for i in self.element[1:]:
            txt.insert(tk.INSERT, f"\n{i}")

queue = Queue()

top = Tk()
top.geometry("700x500")
top.title("Queue")

txt = Text(top, width=60, height=15)
txt.place(x=100, y=50)

ent = Entry(top, width=60)
ent.place(x=100, y=305)

txt.insert(tk.INSERT, """To enqueue enter the name and then click "Enqueue"\nTo dequeue click "Dequeue"\nTo display the queue click "Display Queue" """)

def show(x):
    if x == "enq":
        name = ent.get()
        queue.element.append(name)
        ent.delete(0, tk.END)
        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT, "Name Queued")

    elif x == "deq":
        queue.element.pop(0)
        ent.delete(0, tk.END)
        txt.delete("1.0", tk.END)
        txt.insert(tk.INSERT, "Name Dequeued")

    elif x == "dis":
        txt.delete("1.0", tk.END)
        queue.dis_queue()

enq = Button(top, text="Enqueue", width=20, height=2, command=lambda: show("enq"))
enq.place(x=100, y=330)

deq = Button(top, text="Dequeue", width=20, height=2, command=lambda: show("deq"))
deq.place(x=100, y=380)

dis = Button(top, text="Display Queue", width=20, height=2, command=lambda: show("dis"))
dis.place(x=100, y=430)

top.mainloop()



