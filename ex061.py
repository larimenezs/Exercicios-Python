#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.


print('Gerador de PA')
print('-='*12)
p_termo = int(input('Primeiro termo:'))
raz = int(input('Razão da PA:')) #o tanto de pulos.
c = 1 #pq a gnt começa contar do 1 e ele quer 10 termos.
while c <= 10:
        print(f'{p_termo}', end=' ')
        p_termo += raz
        c += 1
print('Fim!')