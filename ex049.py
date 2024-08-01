#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher.
#Só que agora utilizando um laço for.


num = int(input('Digite um número para ver sua tabuada:'))
for number in range(1, 11):
    print(f'{num} X {number} = {num*number}')

