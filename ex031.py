#Desenvolva um programa que pergunta a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200Km e R$0.45 para viagens mais longas.

distance = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {distance}')
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f'E o preço da sua viagem será R${price}')