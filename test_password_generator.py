import random
import string


def password_generator(len_pass = 12):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ''

    for c in range(0, len_pass):
        digit = random.choice(options)
        password_user += digit
    
    return password_user


choice_user = input('Quantos digitos deseja na senha? ')

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print('ERRO! Entrada inválida!')
    quit()

response = password_generator(len_pass=choice_user)
print(f'Sua senha gerada é: {password_generator(len_pass=choice_user)}')