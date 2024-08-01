# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o seno de {seno}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o cosseno de {cosseno}')
tangente = tan(radians(ângulo))
print(f'A ângulo de {ângulo} tem a tangente de {tangente}')