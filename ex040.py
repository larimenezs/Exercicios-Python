# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
# final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO


grade1 = float(input('Primeira nota:'))
grade2 = float(input('Segunda nota:'))
average = (grade1 + grade2) / 2
print(f'Tirando {grade1} e {grade2} a média é {average}')
if average < 5:
    print('Você foi REPROVADO!!!')
elif (average <= 6.9):
    print('Você ficou de RECUPERAÇÃO!!!')
else:
    print('Você foi APROVADO!!!')

