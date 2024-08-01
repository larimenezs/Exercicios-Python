# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.


salary = float(input('Qual é o salário do funcionário? R$'))
height = salary + salary * 0.10
below = salary + salary * 0.15
if salary > 1250:
    print(f'Quem ganhava {salary} passa a ganhar {height} agora')
else:
    print(f'Quem ganhava {salary} passa a ganhar {below} agora')