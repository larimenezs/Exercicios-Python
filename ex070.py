#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar. No final mostre:
#A)Qual é o total gasto na compra; B)Quantos produtos custam mais de R$1000;
#C)Qual é o nome do produto mais barato.


print('-='*15)
print('LOJA SUPER BARATÃO')
print('-='*15)
tot = tot1000 = menor = cont = 0
barato = ' '
while True:
    product = str(input('Nome do produto:')).strip().upper()
    price = int(input('Preço: R$'))
    cont += 1
    tot += price
    if price > 1000:
        tot1000 += 1
    if cont == 1 or price < menor:
        menor = price
        barato = product
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('------------- FIM DO PROGRAMA ---------------')
print(f'O total da compra foi R${tot}')
print(f'Temos {tot1000} produto/produtos custando mais de R$1000 reais')
print(f'O produto mais barato foi {barato} que custa {menor}')
