#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for impar, desconsidere-o.


s = 0
c = 0
for cont in range(1, 7):
    num = int(input(f'Digite o {cont} valor:'))
    if num % 2 == 0:
        s += num
        c += 1
print(f'Você informou {c} números pares e a soma foi {s}')


