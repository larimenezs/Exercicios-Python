#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

number = int(input('Digite um número qualquer?'))
if number % 2 == 0:
    print(f'O número {number} é par!')
else:
    print(f'O número {number} é impar!')
