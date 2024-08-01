# Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Fatorial de:'))
c = num
f = 1
print(f'Calculando {num}! = ', end='')
while c > 0:
    print(f'{c}', end=' ')
    print(f'x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)