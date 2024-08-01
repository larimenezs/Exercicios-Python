# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar().A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a
# segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.


from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(0, 5): #p/ contar 5 números
        n = randint(1, 10) #escolhe os 5 números sorteados
        lista.append(n)
        print(f' {n}' , end='', flush=True)
        sleep(0.3)
    print(' Pronto!')



def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor  #+1 é quando é looping
    print(f'Somando os valores pares de {lista}, temos {soma}.')


números = list()
sorteia(números)
somaPar(números)

