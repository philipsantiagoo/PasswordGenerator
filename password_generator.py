# Bibliotecas usadas
# random: Para gerar números aleatórios
# string: Para usar os caracteres disponíveis para a senha
# time: Para fazer uma pausa entre as mensagens
import random
import string
from time import sleep


# Função para gerar a senha
def password_generator(choose_digits, choose_numbers='n', choose_uppercase='n', choose_lowercase='n', choose_special='n'): 
    numbers_options = string.digits
    uppercase_options = string.ascii_uppercase
    lowercase_options = string.ascii_lowercase
    special_options = string.punctuation


    options = ''

    if choose_numbers == 's':
       options += numbers_options
    if choose_uppercase == 's':
        options += uppercase_options
    if choose_lowercase == 's':
        options += lowercase_options
    if choose_special == 's':
        options += special_options

    if not options:
        return "ERRO! Nenhum tipo de caractere selecionado!"
    

    password_user = ''

    for c in range(choose_digits):
        digit = random.choice(options)
        password_user += digit
    
    return password_user


# Programa principal
choose_digits = input('Quantos digitos deseja na sua senha? ')
choose_numbers = input('Deseja números? [s/n]: ').lower()[0]
choose_uppercase = input('Deseja letras maiúsculas? [s/n]: ').lower()[0]
choose_lowercase = input('Deseja letras minúsculas? [s/n]: ').lower()[0]
choose_special = input('Deseja caracteres especiais? [s/n]: ').lower()[0]


if choose_digits.isdigit():
    choose_digits = int(choose_digits)
else: 
    print('ERRO! Entrada inválida!')
    quit()


response = password_generator(choose_digits=choose_digits, choose_numbers=choose_numbers, choose_uppercase=choose_uppercase, choose_lowercase=choose_lowercase, choose_special=choose_special)
sleep(1)
print('=' * 30)
sleep(1)
print(f'Sua senha gerada é: {response}')
print('Se não gostar, basta gerar outra!')