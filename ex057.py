# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.


sex = str(input('Informe seu sexo [F/M]:')).strip().upper()[0]
while sex not in 'MmFf':
    sex = str(input(f'Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print(f'Sexo {sex} registrado com sucesso!')







