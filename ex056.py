# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.


somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0
for people in range(1, 5):
    print(f'--------- {people} PESSOA ----------')
    name = str(input('Nome:')).strip()
    age = int(input('Idade:'))
    sex = str(input('Sexo [F/M]:')).strip()
    somaidade += age
    if people == 1 and sex in 'Mm':
        maioridadedehomem = age
        nomevelho = name
    if sex in 'Mm' and age > maioridadedehomem:
        maioridadedehomem = age
        nomevelho = name
    if sex in 'Fm' and age < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulher/mulheres com menos de 20 anos.')
