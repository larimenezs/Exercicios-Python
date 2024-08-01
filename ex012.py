#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


product = float(input('Qual é o preço do produto? R$'))
discount = product - product * 0.05
print(f'O produto que custava {product}, na promoção com desconto de 5%, vai custar {discount}.')

