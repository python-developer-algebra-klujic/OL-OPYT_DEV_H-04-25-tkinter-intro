import random
import tkinter as tk


def password_generator():
    password = ''
    characters = [chr(i) for i in range(33, 127)]
    random.shuffle(characters)

    for letter in characters[ : scl_password_lenght_var.get()]:
        password += letter
    lbl_password_var.set(password)


def save_password():
    root.clipboard_clear()
    root.clipboard_append(lbl_password_var.get())


def reset_password():
    lbl_password_var.set('Generate new password')



root = tk.Tk()
root.title('Password Generator')
root.geometry('600x400')

lbl_title = tk.Label(root,
                     text='Python Generator',
                     font=('Verdana', 20))
lbl_title.grid(column=0, columnspan=3, row=0, padx=10, pady=10, ipadx=5, ipady=5)

lbl_password_var = tk.StringVar(root, '!Pa$$w0rd!')
lbl_password = tk.Label(root,
                        textvariable=lbl_password_var,
                        font=('Verdana', 25))
lbl_password.grid(column=0, columnspan=3, row=1, padx=10, pady=10, ipadx=5, ipady=5)

btn_generate_pwd = tk.Button(root,
                             text='generate',
                             font=('Verdana', 18),
                             command=password_generator)
btn_generate_pwd.grid(column=0, row=2, padx=10, pady=10, ipadx=5, ipady=5)
btn_save_pwd = tk.Button(root,
                         text='save',
                         font=('Verdana', 18),
                         command=save_password)
btn_save_pwd.grid(column=1, row=2, padx=10, pady=10, ipadx=5, ipady=5)
btn_reset_pwd = tk.Button(root,
                          text='reset',
                          font=('Verdana', 18),
                          command=reset_password)
btn_reset_pwd.grid(column=2, row=2, padx=10, pady=10, ipadx=5, ipady=5)


scl_password_lenght_var = tk.IntVar(root, 10)
scl_password_lenght = tk.Scale(root,
                               length=300,
                               from_= 8,
                               to= 40,
                               orient='horizontal',
                               font=('Verdana', 18),
                               variable=scl_password_lenght_var)
scl_password_lenght.grid(column=0, columnspan=3, row=3, padx=10, pady=10, ipadx=5, ipady=5)

# Izbor kompleksnosti passworda
# samo brojevi
# brojevi i slova
# sve

lbl_settings_frame = tk.LabelFrame(root, text='Postavke')
lbl_settings_frame.grid(column=0, columnspan=3, row=4, padx=10, pady=10, ipadx=5, ipady=5)


root.mainloop()
