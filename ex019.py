# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
student1 = input('Primeiro aluno:')
student2 = input('Segundo aluno:')
student3 = input('Terceiro aluno:')
student4 = input('Quarto aluno:')
list = [student1, student2, student3, student4]
drawn = random.choice(list)
print(f'O aluno escolhido foi {drawn}')
