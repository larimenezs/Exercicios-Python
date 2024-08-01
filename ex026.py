#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase:')).strip().upper()
print(f'A letra A aparece {phrase.count('A')} vezes.')
print(f'A primeira letra A apareceu na posição {phrase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {phrase.rfind('A')+1}')




