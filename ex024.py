#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Em que cidade você nasceu?')).strip()
print(city[:5].upper() == 'SANTO')
