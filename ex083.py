#Crie um programa onde o usuário digite uma expressão qualquer que use parêntases.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expr = str(input('Digite a expressão:'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':  #')' eu tenho 2 possibilidades = ou lista tá cheia ou lista tá vazia
        if len(pilha) > 0: #sinal que a lista tá cheia
            pilha.pop() #remove o último elemento
        else: #lista tá vazia
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('sua expressão está errada!')