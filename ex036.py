# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.


value_house = float(input('Valor da casa:'))
salary = float(input('Salário do comprador:'))
years_financing = int(input('Quantos anos de financiamento?'))
portion = value_house / (years_financing * 12) #valor da parcela
min = salary * 30 / 100 #O valor da prestação mensal ñ pode exceder 30% do valor do salário
if portion <= min: #não excedeu os 30%
    print('Seu empréstimo bancário foi aprovado!')
    print(f'Para pagar uma casa de R${value_house} em {years_financing} anos, a prestação será de R${portion}.')
else:
    print('Empréstimo NEGADO!')

