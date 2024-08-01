# Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastreo-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


valores = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar.')
    r = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')