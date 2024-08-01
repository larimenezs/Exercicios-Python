#Faça um programa que leia o nome completo de uma pessoa.
#Mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome completo:')).strip()
n= name.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')









