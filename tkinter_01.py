import os
import tkinter as tk


def increment():
    lbl_counter_var.set(lbl_counter_var.get() + 1)

def decrement():
    lbl_counter_var.set(lbl_counter_var.get() - 1)


root = tk.Tk()
root.title('TkInter DEMO')
root.geometry('600x400')

lbl_title = tk.Label(root,
                     text='Pozdrav iz TkIntera!',
                     font=('Verdana', 18))
lbl_title.pack(padx=10, pady=10)
lbl_subtitle = tk.Label(root,
                        text='Ovo je moja prva TkInter aplikacija',
                        font=('Verdana', 14))
lbl_subtitle.pack(padx=10, pady=10)


btn_increment = tk.Button(root,
                          text='Increment (+)',
                          font=('Verdana', 14),
                          command=increment)
btn_increment.pack(padx=10, pady=10)
btn_decrement = tk.Button(root,
                          text='Decrement (-)',
                          font=('Verdana', 14),
                          command=decrement)
btn_decrement.pack(padx=10, pady=10)

lbl_counter_var = tk.DoubleVar(root, 0)
lbl_counter = tk.Label(root,
                       textvariable=lbl_counter_var,
                       font=('Verdana', 25))
lbl_counter.pack(padx=10, pady=10)


root.mainloop()
