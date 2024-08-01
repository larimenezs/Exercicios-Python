# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão.


number = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
option = int(input('Sua opção:'))
if option == 1:
    print(f'Convertido para binário é igual a {bin(number)}')
elif option == 2:
    print(f'Convertido para octal é igual a {oct(number)}')
elif option == 3:
    print(f'Convertido para hexadecimal é igual a {hex(number)}')