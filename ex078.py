# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No fina, mostre qual foi
# o maior e o menor valor digitado e as suas respectivas posições na lista.


listnum = []
maior = menor = 0
for c in range(0, 5):
    listnum.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        maior = menor = listnum[c]
    else:
        if listnum[c] > maior:
            maior = listnum[c]
        if listnum[c] < menor:
            menor = listnum[c]
print('=-' * 30)
print(f'Você digitou os valores {listnum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listnum):  #para aparecer o índice do valor.
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listnum):  #para aparecer o índice do valor.
    if v == menor:
        print(f'{i}... ', end='')
print()
