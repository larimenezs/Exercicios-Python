#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m².


width = float(input('Largura da parede:'))
height = float(input('Altura da parede:'))
a = width * height
ink = a / 2
print(f'Sua parede tem dimensão de {width}x{height} e sua área é de {a}m2.')
print(f'Para pintar a sua parede, você precisará de {ink}L de tinta.')

