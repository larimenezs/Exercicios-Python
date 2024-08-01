# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo!')
    if (a == b) and (a == c):
        print('Triângulo Equilátero, pois os três lados são iguais.')
    elif (a == b) or (a == c) or (b == c):
        print('Triângulo Isósceles, pois tem pelo menos dois lados iguais.')
    else:
        print('Triângulo Escaleno, pois todos os lados são diferentes.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')

