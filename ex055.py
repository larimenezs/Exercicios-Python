# Faça um programa que leia o peso dee cinco pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.


maior = 0
menor = 0
for people in range(1, 6):
    weight = float(input(f'Peso da {people} pessoa:'))
    if people == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior:
            maior = weight
        if weight < menor:
            menor = weight
print(f'O maior peso lido foi de {maior}')
print(f'O menor peso lido foi de {menor}')