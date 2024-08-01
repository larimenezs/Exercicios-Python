#Desenvolva um programa que leia o primeiro termo ea razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.


print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
first = int(input('Primeiro termo:'))
raz = int(input('Razão:'))
ten = first + (10 - 1) * raz
for c in range(first, ten + raz, raz):
    print(c)
print('ACABOU!')