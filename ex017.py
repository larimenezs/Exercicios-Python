# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.


import math
cateto_o = float(input('comprimento do cateto oposto:'))
cateto_a = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(cateto_o, cateto_a)
print(f'A hipotenusa vai medir {h}')

'''co= float(input('Comprimento do cateto oposto?'))
ca= float(input('Comprimento do cateto adjacente?'))
h = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {h}')'''


