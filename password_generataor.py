import random
import tkinter as tk


PWD_LENGHT = 15

def password_generator():
    password = ''
    characters = [chr(i) for i in range(33, 127)]
    random.shuffle(characters)

    for letter in characters[ : PWD_LENGHT]:
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


root.mainloop()
