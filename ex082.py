# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


listatot = []
listapar = []
listaimpar = []
while True:
    listatot.append(int(input('Digite um número:')))
    resp = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
for c in listatot:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'A lista completa é {listatot}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')