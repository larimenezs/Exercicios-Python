#Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
#Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo;
#Abaixo de 18.5;Abaixo do Peso
#Entre 18.5 e 25;Peso Ideal
#25 até 30;Sobrepeso
#30 até 40;Obesidade
#Acima de 40;Obesidade Mórbida


weith = float(input('Qual é o seu peso?'))
height = float(input('Qual é a sua altura?'))
imc = weith / height ** 2
if imc < 18.5:
    print(f'O imc dessa pessoa é de {imc}')
    print('Você está abaixo do peso ideal.')
elif imc <25:
    print(f'O imc dessa pessoa é de {imc}')
    print('Você está no peso ideal.')
elif imc <30:
    print(f'O imc dessa pessoa é de {imc}')
    print('Você está com sobrepeso.')
elif imc <40:
    print(f'O imc dessa pessoa é de {imc}')
    print('Você está com obesidade.')
else:
    print(f'O imc dessa pessoa é de {imc}')
    print('Você está com obesidade morbida.')