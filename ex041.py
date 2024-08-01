# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER


from datetime import date
born = int(input('Ano de nascimento:'))
current_year = date.today().year - born
print(f'O atleta tem {current_year} anos.')
if current_year <= 9:
    print('CLASSIFICAÇÃO: Mirim')
elif current_year <= 14:
    print('CLASSIFICAÇÃO: Infantil')
elif current_year <= 19:
    print('CLASSIFICAÇÃO: Junior')
elif current_year <= 25:
    print('CLASSIFICAÇÃO: Sênior')
else:
    print('CLASSIFICAÇÃO: Master')
