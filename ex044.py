#Elabore um programa que calcula o valor a ser pago por um produto.
#Considerando o seu preço normal e condição de pagamento;
#Á vista dinheiro/cheque; 10% de desconto
#Á vista no cartão; 5% de desconto
#Em até 2x no cartão; Preço normal
#3x ou mais no cartão; 20% de juros


print('='*13)
print('Loja Menezes')
print('='*13)
price = float(input('Preço das compras:'))
print('''Formas de pagamentos
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
option = int(input('Qual a opção:'))
if option == 1:
    balance = price - price * 10 / 100
    print(f'Sua compra de {price} a vista no dinheiro/cheque é de {balance}.')
elif option == 2:
    balance = price - price * 5 / 100
    print(f'Sua compra de {price} a vista no cartão é de {balance} sem juros.')
elif option == 3:
    balance = price / 2
    print(f'Sua compra de {price} parcelada em 2X no cartão é de {balance} sem juros.')
else:
    balance = price + price * 20 /100
    portion = int(input('Quantas parcelas?'))
    t = balance / portion
    print(f'Sua compra de {price} parcelada em {portion}X no cartão é de {t}.')

