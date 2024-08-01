# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade se ele
# ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo de
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
current_year = date.today().year
born = int(input('Ano de nascimento:'))
age = current_year - born
print(f'Quem nasceu em {born} tem {age} anos em {current_year}')
if age < 18:
    balance = 18 - age
    print(f'Ainda você não pode se alistar, faltam {balance} anos.')
    print(f'Seu alistamento será em {current_year + balance}.')
elif age > 18:
    balance = age - 18
    print(f'Você já passou {balance} anos de se alistar.')
    print(f'Seu alistamento foi em {current_year - balance}.')
else:
    print(f'Você precisa se alistar ainda esse ano!')



