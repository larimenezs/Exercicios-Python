#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre: A)Quantas pessoas tem mais de 18 anos; B)Quantos homens foram cadastrados;
#C)Quantas mulheres tem menos de 20 anos.


print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
maior18 = men = woman20 = 0
while True:
    age = int(input('Idade:'))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo: [M/F]')).strip().upper()[0]
    if age >= 18:
        maior18 += 1
    if sex == 'M':
        men += 1
    if sex == 'F' and age < 20:
        woman20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos é {maior18}')
print(f'Ao todo temos {men} homem/homens cadastrados')
print(f'E temos {woman20} mulher/mulheres com menos de 20 anos')