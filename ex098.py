# Faça um programa que tenha uma função chamada contador(), que receba três parâmentros
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


from time import sleep

def contador(i, f, p): #início, fim e passo
    if p <= 0:
        p *= -1 #trocando o sinal dele, fazendo virar positivo (negativo com negativo = positivo)
                # -1 pq o 1 não altera o valor que a pessoa digitou
    if p == 0:
        p = 1  #se digitar 0, será considerado como 1
    print('-=' * 20)
    print(f'Contando de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f: #no caso do início ser menor que o fim
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')

    else: #no caso do início ser maior que o fim
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2) #início maior que o fim
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)


