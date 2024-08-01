#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.


print('Gerador de PA')
print('-='*15)
p_termo = int(input('Primeiro termo:'))
raz = int(input('Razão da PA:'))
termo = p_termo
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo}', end=' ')
        termo += raz
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')



