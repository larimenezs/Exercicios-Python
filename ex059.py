# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# Seu programa deverá realizar a operação solicitada em cada caso.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa


print('=-='*10)
value1 = float(input('Primeiro valor:'))
value2 = float(input('Segundo valor:'))
option = 0
while option != 5:
    print('''
    [1] Somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    option = int(input('>>>>> Qual é a sua opção?'))
    if option == 1:
        sum1 = value1 + value2
        print(f'A soma entre {value1} + {value2} é {sum1}')
    elif option == 2:
        mult = value1 * value2
        print(f'A multiplicação entre {value1} x {value2} é {mult}')
    elif option == 3:
        if value1 > value2:
            maior = value1
        else:
            maior = value2
        print(f'Entre {value1} e {value2} o maior valor é {maior}')
    elif option == 4:
        print('Informe os números novamente:')
        value1 = int(input('Primeiro valor: '))
        value2 = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...!')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
print('Fim do Programa!!! Volte sempre.')





