import os
import tkinter as tk


def btn_clicked():
    print('Gumb je kliknut.')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


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


btn_click = tk.Button(root,
                      text='Klikni me!',
                      font=('Verdana', 14),
                      command=btn_clicked)
btn_click.pack(padx=10, pady=10)

btn_clear_terminal = tk.Button(root,
                              text='Ocisti terminal',
                              font=('Verdana', 14),
                              command=clear_terminal)
btn_clear_terminal.pack(padx=10, pady=10)

root.mainloop()
