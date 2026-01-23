import random
import tkinter as tk


def password_generator():
    # posebni znakovi   33-47 | 58-64 | 91-96 | 123 - 126
    # brojevi           48-57
    # slova             65-90 | 97-122
    # sve               33-126

    password = ''
    pwd_lenght = scl_password_lenght_var.get()

    characters = list(range(33, 47))
    characters.extend(list(range(58, 64+1)))
    characters.extend(list(range(91, 96+1)))
    characters.extend(list(range(123, 126+1)))
    random.shuffle(characters)
    all_characters = [chr(i) for i in characters]

    numbers = list(range(48, 57+1))
    # random.shuffle(numbers)
    all_numbers = [chr(i) for i in numbers]

    letters = list(range(65, 90+1))
    letters.extend(list(range(97, 122+1)))
    random.shuffle(letters)
    all_letters = [chr(i) for i in letters]

    if ck_chars_var.get():
        for char in all_characters[ : pwd_lenght]:
            password += char
        lbl_password_var.set(password)

    if ck_numbers_var.get():
        for _ in range(pwd_lenght):
            password += random.choice(all_numbers)
        lbl_password_var.set(password)

    if ck_letters_var.get():
        for letter in all_letters[ : pwd_lenght]:
            password += letter
        lbl_password_var.set(password)

    if not ck_chars_var.get() and not ck_letters_var.get() and not ck_numbers_var.get():
        complex_pwd = list(range(33, 126))
        random.shuffle(complex_pwd)
        all_complex_pwd = [chr(i) for i in complex_pwd]

        for letter in all_complex_pwd[ : pwd_lenght]:
            password += letter
        lbl_password_var.set(password)


def save_password():
    root.clipboard_clear()
    root.clipboard_append(lbl_password_var.get())


def reset_password():
    lbl_password_var.set('Generate new password')
    scl_password_lenght_var.set(10)
    ck_chars_var.set(False)
    ck_letters_var.set(False)
    ck_numbers_var.set(False)


def toggle_password():
    if toggle_password_var.get() == 'display':
        lbl_password.config(show='')
    else:
        lbl_password.config(show='*')



root = tk.Tk()
root.title('Password Generator')



lbl_title = tk.Label(root,
                     text='Python Generator',
                     font=('Verdana', 20))
lbl_title.grid(column=0, columnspan=3, row=0, padx=10, pady=10, ipadx=5, ipady=5)



lbl_password_var = tk.StringVar(root, '!Pa$$w0rd!')
lbl_password = tk.Entry(root,
                        textvariable=lbl_password_var,
                        justify='center',
                        width=45,
                        background='systembuttonface',
                        border=0,
                        show='*', # Omoguciti izbor nakon pauze!!!
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



lbl_settings_frame = tk.LabelFrame(root, text='Postavke')
lbl_settings_frame.grid(column=0, columnspan=3, row=4, padx=10, pady=10, ipadx=5, ipady=5)

ck_numbers_var = tk.BooleanVar()
ck_numbers = tk.Checkbutton(lbl_settings_frame,
                            text='Brojevi',
                            variable=ck_numbers_var)
ck_numbers.grid(column=0, row=0, padx=10, pady=10, ipadx=5, ipady=5)
ck_letters_var = tk.BooleanVar()
ck_letters = tk.Checkbutton(lbl_settings_frame,
                            text='Slova',
                            variable=ck_letters_var)
ck_letters.grid(column=1, row=0, padx=10, pady=10, ipadx=5, ipady=5)
ck_chars_var = tk.BooleanVar()
ck_chars = tk.Checkbutton(lbl_settings_frame,
                          text='Znakovi',
                          variable=ck_chars_var)
ck_chars.grid(column=2, row=0, padx=10, pady=10, ipadx=5, ipady=5)


toggle_password_var = tk.StringVar(value='hide')
rb_display_pwd = tk.Radiobutton(lbl_settings_frame,
                                text='Prikazi password',
                                variable=toggle_password_var,
                                value='display',
                                command=toggle_password)
rb_display_pwd.grid(column=0, row=1, padx=10, pady=10, ipadx=5, ipady=5)

rb_hide_pwd = tk.Radiobutton(lbl_settings_frame,
                             text='Sakrij password',
                             variable=toggle_password_var,
                             value='hide',
                             command=toggle_password)
rb_hide_pwd.grid(column=2, row=1, padx=10, pady=10, ipadx=5, ipady=5)





root.mainloop()
