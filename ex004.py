#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ele.

something = input('Digite algo:')
print(type(something))
print('Só tem espaços?', something.isspace())
print('É um número?', something.isnumeric())
print('É alfabético?', something.isalpha())
print('É alfanumérico?', something.isalnum())
print('Está em maiúsculas?', something.isupper())
print('Está em minúsculas?', something.islower())
print('Está capitalizada?', something.istitle())




