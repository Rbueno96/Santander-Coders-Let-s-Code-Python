"""Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação
inválida."""

idade = int(input('Qual é a sua idade? '))
while idade < 0 or idade > 150:
    print(f'Erro. {idade} não é uma idade válida.')
    idade = int(input('Qual é a sua idade? '))
print()
salario = float(input('Qual é o seu salário em reais? R$'))
while salario < 0:
    print(f'Erro. O salário {salario} não é válido.')
    salario = float(input('Qual é o seu salário em reais? R$'))
print()
while True:
    sexo = str(input('Qual é o seu sexo? [M/F/OUTRO]: ')).upper().strip()
    if sexo == 'M':
        sexo = 'masculino'
        break
    elif sexo == 'MASCULINO':
        sexo = 'masculino'
        break
    elif sexo == 'FEMININO':
        sexo = 'feminino'
        break
    elif sexo == 'F':
        sexo = 'feminino'
        break
    elif sexo == '':
        sexo = 'não informado'
        break
    elif sexo == 'OUTRO':
        sexo = 'outro'
        break
    elif sexo == 'MF':  # Não consigo resolver esse problema do MF
        print(f'Erro. "{sexo.lower()}" não é uma opção de válida.')
        sexo = 'não definido'
        continue
    else:
        print(f'Erro. "{sexo.lower()}" não é uma opção de válida.')
        continue
print(f'Você tem {idade}, seu salário é de R${salario} e você é do sexo {sexo}.')
