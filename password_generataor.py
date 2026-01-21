import random
# svi znakovi su od 33 - 126


password_length = 15
characters = [chr(i) for i in range(33, 127)]
random.shuffle(characters)
password = ''
for letter in characters[ : password_length]:
    password += letter

print(password)

'''
PASWORD GENERATOR

PASSWORD VALUE - default value '!Pa$$w0rd!'

[generate password]
'''