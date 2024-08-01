#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
ram = randint(0,5)
#print(f'Pensei no número: {ram}')
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
player = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if player == ram:
    print('PARABÉNS! Você conseguiu me vencer')
else:
    print('GANHEI! Tente novamente!')
