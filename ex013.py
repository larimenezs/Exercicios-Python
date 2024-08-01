#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo sálario, com 15% de aumento.


salary = float(input('Qual é o salário do funcionário? R$'))
new_salary = salary + salary * 0.15
print(f'Um funcionário que ganhava {salary}, com 15% de aumento, passa a receber {new_salary}.')
