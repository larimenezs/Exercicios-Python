#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite.

speed = float(input('Qual é a velocidade atual do carro?'))
if speed > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade permitido que é 80km/h.')
    ticket = (speed - 80) * 7
    print(f'Você deve pagar uma multa de {ticket}')
print('Tenha um bom dia! Dirija com segurança.')