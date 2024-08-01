#Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, m, dm, cm e mm.

value = float(input('Uma distância em metros:'))
km = value / 1000
hm= value / 100
dam = value / 10
dm = value * 10
cm = value * 100
mm = value * 1000
print(f'A medida de {value} corresponde a \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')





