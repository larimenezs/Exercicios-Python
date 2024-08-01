#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem consider espaços).
#Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome completo:'))
print('Analisando seu nome...')
max = print(f'Seu nome em MAIÚSCULAS é {name.upper()}')
min = print(f'Seu nome em minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(' ')}')
print(f'Seu primeiro nome tem {name.find(' ')} letras')



