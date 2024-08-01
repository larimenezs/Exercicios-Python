# Crie um programa que leia o ao de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date
data = date.today().year
totmaior = 0
totmenor = 0
for people in range(1, 8):
    born = int(input(f'Em que ano a {people} pessoa nasceu?'))
    age = data - born
    if age >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade')
print(f'Ao todo tivemos {totmenor} menores de idade')
