#Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.


phrase = str(input('Digite uma frase:')).strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = ''
for letter in range(len(together) - 1, -1, -1):
    reverse += together[letter]
print(f'O inverso de {together} é {reverse}')
if reverse == together:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')