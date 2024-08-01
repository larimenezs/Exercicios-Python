#Crie um programa que faça o computador jogar Jokenpô com você.


from random import randint
from time import sleep
ram = ('pedra', 'papel', 'tesoura')
computer = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
play = int(input('Qual é a sua jogada?'))
print('''JO
KEN
PO!!''')
sleep(2)
print('-='*20)
print(f'Computador jogou {ram[computer]}')
print(f'Jogador jogou {ram[play]}')
print('-='*20)
if computer == 0:
    if play == 0:
        print('EMPATOU!')
    elif play == 1:
        print('Você GANHOU!')
    elif play == 2:
        print('Computador GANHOU!')
    else:
        print('Jogada Inválida!')
elif computer == 1:
    if play == 0:
        print('Computador GANHOU!')
    elif play == 1:
        print('EMPATOU!')
    elif play == 2:
        print('Você GANHOU!')
    else:
        print('Jogada Inválida!')
elif computer == 2:
    if play == 0:
        print('Você GANHOU!')
    elif play == 1:
        print('Computador GANHOU!')
    elif play == 2:
        print('EMPATOU!')
    else:
        print('Jogada Inválida!')

