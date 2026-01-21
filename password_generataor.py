import random
import tkinter as tk


def password_generator():
    password = ''
    characters = [chr(i) for i in range(33, 127)]
    random.shuffle(characters)

    for letter in characters[ : scl_password_lenght_var.get()]:
        password += letter
    lbl_password_var.set(password)


root = tk.Tk()
root.title('Password Generator')

lbl_title = tk.Label(root,
                     text='Python Generator',
                     font=('Verdana', 20))
lbl_title.pack(padx=10, pady=15)

lbl_password_var = tk.StringVar(root, '!Pa$$w0rd!')
lbl_password = tk.Label(root,
                        textvariable=lbl_password_var,
                        font=('Verdana', 25))
lbl_password.pack(padx=10, pady=15)

btn_generate_pwd = tk.Button(root,
                             text='generate password',
                             font=('Verdana', 18),
                             command=password_generator)
btn_generate_pwd.pack(padx=10, pady=15)

scl_password_lenght_var = tk.IntVar(root, 10)
scl_password_lenght = tk.Scale(root,
                               length=300,
                               from_= 8,
                               to= 40,
                               orient='horizontal',
                               font=('Verdana', 18),
                               variable=scl_password_lenght_var)
scl_password_lenght.pack(padx=10, pady=15)

root.mainloop()
